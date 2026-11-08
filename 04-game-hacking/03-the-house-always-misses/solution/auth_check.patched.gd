extends Control

@onready var status_label: Label = $StatusLabel
@onready var continue_button: Button = $ContinueButton

const CHALLENGE_ID: int = 49
const API_BASE: String = "https://pointeroverflowctf.com"
const INSTANCE_URL: String = API_BASE + "/api/challenges/%d/instance"



const GAME_SCENE: PackedScene = preload("res://scenes/game/gallery.tscn")

var _ok: bool = false
var _http: HTTPRequest

func _ready() -> void :
	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
	get_tree().paused = false
	continue_button.disabled = true
	continue_button.pressed.connect(_on_continue_pressed)
	status_label.text = "Checking access..."
	_http = HTTPRequest.new();add_child(_http)
	_http.use_threads = true;_http.timeout = 10.0
	_http.process_mode = Node.PROCESS_MODE_ALWAYS
	_validate()

func _on_continue_pressed() -> void :
	if not _ok: return
	get_tree().change_scene_to_packed(GAME_SCENE)

func _validate() -> void :
	print("VALIDATE start")
	var token: = _read_text_file("game.token")
	var team_key: = _read_text_file("team.key")
	if token.is_empty(): status_label.text = "Missing game.token";return
	if team_key.is_empty(): status_label.text = "Missing team.key";return
	Session.game_token = token;Session.team_key = team_key;Session.nonce = ""
	var url: = INSTANCE_URL % CHALLENGE_ID
	var headers: PackedStringArray = [
		"X-POCTF-GAME-TOKEN: " + token, 
		"X-POCTF-TEAM-KEY: " + team_key, 
	]
	_http.request_completed.connect(_on_instance_done, CONNECT_ONE_SHOT)
	_http.request(url, headers)

func _on_instance_done(result: int, code: int, _hdrs: PackedStringArray, body: PackedByteArray) -> void :
	print("AUTH result=",result," code=",code," body=",body.get_string_from_utf8().substr(0,120))
	if result != HTTPRequest.RESULT_SUCCESS or code != 200:
		status_label.text = "Auth failed (result=%d code=%d)" % [result, code]
		return
	var parsed: Variant = JSON.parse_string(body.get_string_from_utf8())
	if typeof(parsed) != TYPE_DICTIONARY or not (parsed as Dictionary).has("nonce"):
		status_label.text = "Bad response / missing nonce";return
	var d: = parsed as Dictionary
	Session.nonce = str(d["nonce"])
	if d.has("team_id"): Session.team_id = int(d["team_id"])
	_ok = true
	status_label.text = "Access granted. Good luck."
	continue_button.disabled = false;continue_button.grab_focus()
	call_deferred("_on_continue_pressed")

func _read_text_file(filename: String) -> String:
	var path: = "res://" + filename if OS.has_feature("editor") else\
	OS.get_executable_path().get_base_dir().path_join(filename)
	if not FileAccess.file_exists(path): return ""
	var f: = FileAccess.open(path, FileAccess.READ)
	return f.get_as_text().strip_edges() if f else ""
