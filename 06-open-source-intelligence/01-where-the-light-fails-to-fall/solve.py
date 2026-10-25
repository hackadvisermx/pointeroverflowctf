#!/usr/bin/env python3
"""Check the solar position used to identify Baghdad in the OSINT image."""

from datetime import datetime, timezone
from math import acos, atan2, cos, pi, sin, tan


def solar_position(when, latitude, longitude):
    day = when.timetuple().tm_yday
    hour = when.hour + when.minute / 60
    gamma = 2 * pi / 365 * (day - 1 + (hour - 12) / 24)
    equation = 229.18 * (
        0.000075
        + 0.001868 * cos(gamma)
        - 0.032077 * sin(gamma)
        - 0.014615 * cos(2 * gamma)
        - 0.040849 * sin(2 * gamma)
    )
    declination = (
        0.006918
        - 0.399912 * cos(gamma)
        + 0.070257 * sin(gamma)
        - 0.006758 * cos(2 * gamma)
        + 0.000907 * sin(2 * gamma)
        - 0.002697 * cos(3 * gamma)
        + 0.00148 * sin(3 * gamma)
    )
    true_solar_time = (when.hour * 60 + when.minute + 4 * longitude + equation) % 1440
    hour_angle = true_solar_time / 4 - 180
    latitude_rad = latitude * pi / 180
    hour_angle_rad = hour_angle * pi / 180
    zenith = acos(
        sin(latitude_rad) * sin(declination)
        + cos(latitude_rad) * cos(declination) * cos(hour_angle_rad)
    )
    altitude = 90 - zenith * 180 / pi
    azimuth = (
        atan2(
            sin(hour_angle_rad),
            cos(hour_angle_rad) * sin(latitude_rad)
            - tan(declination) * cos(latitude_rad),
        )
        * 180
        / pi
        + 180
    ) % 360
    return azimuth, altitude


if __name__ == "__main__":
    # 17:40 at UTC+03:00 is 14:40 UTC.
    when = datetime(2026, 6, 6, 14, 40, tzinfo=timezone.utc)
    azimuth, altitude = solar_position(when, 33.3152, 44.3661)
    print(f"Baghdad: azimuth={azimuth:.1f}°, altitude={altitude:.1f}°")
