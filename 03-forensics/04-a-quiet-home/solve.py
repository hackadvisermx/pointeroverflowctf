#!/usr/bin/env python3
"""Extract a suspicious device serial from MQTT packets in the capture."""

import argparse
import binascii
import json
import re
import subprocess
import tempfile
import zipfile


TOKEN_RE = re.compile(r"^[A-Z2-7]{16}$")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="downloaded HomeAssistant ZIP")
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive) as archive, tempfile.TemporaryDirectory() as work:
        pcap_name = next(name for name in archive.namelist() if name.endswith(".pcap"))
        pcap_path = f"{work}/capture.pcap"
        with open(pcap_path, "wb") as pcap:
            pcap.write(archive.read(pcap_name))

        command = [
            "tshark", "-r", pcap_path, "-Y", "mqtt", "-T", "fields",
            "-E", "separator=|", "-e", "mqtt.topic", "-e", "mqtt.msg",
        ]
        output = subprocess.check_output(command, text=True)

    for line in output.splitlines():
        fields = line.split("|", 1)
        if len(fields) != 2 or not fields[1]:
            continue
        try:
            payload = json.loads(binascii.unhexlify(fields[1]))
        except (binascii.Error, UnicodeDecodeError, json.JSONDecodeError):
            continue
        serial = payload.get("product_serial")
        if isinstance(serial, str) and TOKEN_RE.fullmatch(serial):
            print(f"{fields[0]}: {serial}")


if __name__ == "__main__":
    main()
