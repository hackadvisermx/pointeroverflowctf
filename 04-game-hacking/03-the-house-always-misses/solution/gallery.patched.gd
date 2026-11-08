




























extends Node2D


@export var duck_scene: PackedScene
@export var civilian_scene: PackedScene
@export var flip_scene: PackedScene
@export var popup_scene: PackedScene


@export var flag_overlay_scene: PackedScene
@export var lose_overlay_scene: PackedScene
@export var help_overlay_scene: PackedScene
@export var crosshair_scene: PackedScene


@export var round_seconds: float = 60.0




@export var score_threshold: int = 1200




@export var initial_duck_interval: float = 3.5
@export var initial_duck_speed: float = 350.0
@export var initial_civilian_ratio: float = 0.125
@export var initial_flip_count: int = 3
@export var initial_popup_interval: float = 3.0


@export var difficulty_step_interval: float = 10.0
@export var difficulty_max_steps: int = 6





@export var duck_group_appear_stream: AudioStream = null


@onready var hud: = $Hud
@onready var targets_root: = $Targets
@onready var crosshair_root: = $CrosshairLayer




@onready var _music: AudioStreamPlayer = $MusicPlayer
@onready var _sfx_start: AudioStreamPlayer = $SfxStart
@onready var _sfx_win: AudioStreamPlayer = $SfxWin
@onready var _sfx_lose: AudioStreamPlayer = $SfxLose
@onready var _sfx_shoot_miss: AudioStreamPlayer = $SfxShootMiss
@onready var _sfx_shoot_hit: AudioStreamPlayer = $SfxShootHit
@onready var _sfx_target_voice: AudioStreamPlayer = $SfxTargetVoice


const BULLET_IMPACT_SCENE: PackedScene = preload("res://scenes/actors/bullet_impact.tscn")



const FLIP_WAVE_COUNT: int = 3
var _flip_wave_index: int = 0
var _flip_hits_this_wave: int = 0


const TickerScript = preload("res://Ticker.gd")
var _ticker: Node = null

var _score: int = 0
var _time_left: float = 0.0
var _elapsed: float = 0.0
var _difficulty: int = 0
var _duck_spawn_timer: float = 0.0
var _popup_spawn_timer: float = 0.0
var _ended: bool = false

var _viewport_size: Vector2


var _esc_down: bool = false
var _help_overlay: CanvasLayer = null


var _m_down: bool = false
var _muted: bool = false





var _voice_owner: Node = null


func _ready() -> void :
	_viewport_size = get_viewport_rect().size
	_time_left = round_seconds
	hud.set_score(_score)
	hud.set_time(_time_left)
	hud.set_threshold(score_threshold)


	if crosshair_scene != null:
		var ch: = crosshair_scene.instantiate()
		crosshair_root.add_child(ch)




	_flip_wave_index = 0
	_spawn_flip_wave()


	_set_ingame_input_mode(true)


	_duck_spawn_timer = 0.3
	_popup_spawn_timer = 1.5



	_ticker = TickerScript.new()
	add_child(_ticker)
	_ticker.call_deferred("start")


func _process(delta: float) -> void :
	if _ended:
		return

	for t in get_tree().get_nodes_in_group("targets"):
		if t is TargetBase and not t._hit and t.points > 0 and t.is_inside_tree():
			t.on_hit()

	_elapsed += delta
	_time_left = max(0.0, _time_left - delta)
	hud.set_time(_time_left)


	var target_step: int = int(_elapsed / difficulty_step_interval)
	if target_step > _difficulty and _difficulty < difficulty_max_steps:
		_difficulty = min(target_step, difficulty_max_steps)




	_duck_spawn_timer -= delta
	if _duck_spawn_timer <= 0.0:
		_duck_spawn_timer = _current_duck_interval()
		if randf() < _current_civilian_ratio():
			_spawn_slider(civilian_scene)
		else:
			_spawn_duck_group()


	_popup_spawn_timer -= delta
	if _popup_spawn_timer <= 0.0:
		_popup_spawn_timer = _current_popup_interval()
		_spawn_popup()


	if _score >= score_threshold:
		_win()
	elif _time_left <= 0.0:
		_lose()


	var esc: bool = Input.is_key_pressed(KEY_ESCAPE)
	if esc and not _esc_down:
		_toggle_help_overlay()
	_esc_down = esc


	var m: bool = Input.is_key_pressed(KEY_M)
	if m and not _m_down:
		_toggle_mute()
	_m_down = m


func _toggle_mute() -> void :
	_muted = not _muted
	AudioServer.set_bus_mute(AudioServer.get_bus_index("Master"), _muted)


func _unhandled_input(event: InputEvent) -> void :
	if _ended:
		return
	if event is InputEventMouseButton and event.pressed:
		var mb: InputEventMouseButton = event as InputEventMouseButton
		if mb.button_index == MOUSE_BUTTON_LEFT:


			if _help_overlay != null and is_instance_valid(_help_overlay):
				return
			_click_at(get_global_mouse_position())






func _click_at(pos: Vector2) -> void :

	_spawn_bullet_marker(pos)

	var space: = get_world_2d().direct_space_state
	var query: = PhysicsPointQueryParameters2D.new()
	query.position = pos
	query.collision_mask = 1
	query.collide_with_areas = true
	query.collide_with_bodies = false
	var results: = space.intersect_point(query, 8)


	var hit_target: TargetBase = null
	for r in results:
		var collider = r.get("collider")
		if collider != null and collider is TargetBase:
			if not (collider as TargetBase)._hit:
				hit_target = collider
				break

	if hit_target != null:

		_play_sfx(_sfx_shoot_hit)



		hit_target.on_hit()
	else:

		_play_sfx(_sfx_shoot_miss)


func _spawn_bullet_marker(pos: Vector2) -> void :
	var mark: = BULLET_IMPACT_SCENE.instantiate() as Node2D
	mark.global_position = pos


	crosshair_root.add_child(mark)







func _hook_target(t: TargetBase) -> void :
	if t == null:
		return
	if t.has_signal("target_appeared"):
		t.target_appeared.connect(_on_target_appeared)
	t.target_hit.connect(_on_target_hit, CONNECT_ONE_SHOT)
	t.target_expired.connect(_on_target_expired, CONNECT_ONE_SHOT)
	if t.has_signal("target_hidden"):
		t.target_hidden.connect(_on_target_hidden)


func _on_target_hit(points: int, target: Node2D) -> void :
	_score += points
	if _score < 0:
		_score = 0
	hud.set_score(_score)



	if target is TargetBase:
		var tb: TargetBase = target
		_play_target_voice(tb, tb.hit_stream)


func _on_target_appeared(target: Node2D) -> void :
	if target is TargetBase:
		var tb: TargetBase = target
		_play_target_voice(tb, tb.appear_stream)


func _on_target_hidden(target: Node2D) -> void :

	_stop_target_voice_if_owned_by(target)


func _on_target_expired(target: Node2D) -> void :

	_stop_target_voice_if_owned_by(target)








func _play_target_voice(owner: Node, stream: AudioStream) -> void :
	if _sfx_target_voice == null:
		return
	if stream == null:


		return
	_voice_owner = owner
	_sfx_target_voice.stop()
	_sfx_target_voice.stream = stream
	_sfx_target_voice.play()


func _stop_target_voice_if_owned_by(owner: Node) -> void :
	if _sfx_target_voice == null:
		return
	if _voice_owner != owner:
		return
	_sfx_target_voice.stop()
	_voice_owner = null


func _play_sfx(p: AudioStreamPlayer) -> void :


	if p == null or p.stream == null:
		return
	p.play()








func _current_flip_positions() -> Array:
	var w: = _viewport_size.x
	var h: = _viewport_size.y
	match _flip_wave_index % FLIP_WAVE_COUNT:
		0:

			return [
				Vector2(w * 0.25, h * 0.28), 
				Vector2(w * 0.5, h * 0.28), 
				Vector2(w * 0.75, h * 0.28), 
			]
		1:

			return [
				Vector2(w * 0.2, h * 0.2), 
				Vector2(w * 0.5, h * 0.42), 
				Vector2(w * 0.8, h * 0.62), 
			]
		_:

			return [
				Vector2(w * 0.1, h * 0.85), 
				Vector2(w * 0.9, h * 0.85), 
				Vector2(w * 0.5, h * 0.15), 
			]


func _spawn_flip_wave() -> void :
	if flip_scene == null:
		return
	var positions: Array = _current_flip_positions()
	_flip_hits_this_wave = 0
	for pos in positions:
		var f: = flip_scene.instantiate() as TargetBase
		targets_root.add_child(f)
		f.global_position = pos
		_hook_target(f)



		f.target_hit.connect(_on_flip_hit, CONNECT_ONE_SHOT)


func _on_flip_hit(_points: int, _target: Node2D) -> void :
	_flip_hits_this_wave += 1
	var wave_size: int = _current_flip_positions().size()
	if _flip_hits_this_wave >= wave_size:
		_flip_wave_index += 1


		call_deferred("_spawn_flip_wave")







func _spawn_duck_group() -> void :
	if duck_scene == null:
		return
	var y: float = randf_range(_viewport_size.y * 0.55, _viewport_size.y * 0.9)
	var going_right: bool = randf() < 0.5
	var speed: float = _current_duck_speed() * (1.0 if going_right else -1.0)
	var spacing: float = 90.0
	var start_x: float = (-30.0 if going_right else _viewport_size.x + 30.0)
	for i in range(5):
		var d: = duck_scene.instantiate() as TargetBase
		targets_root.add_child(d)
		var x_off: float = ( - float(i) * spacing) if going_right\
		else (float(i) * spacing)
		d.global_position = Vector2(start_x + x_off, y)
		if d.has_method("set"):
			d.set("speed", speed)
		_hook_target(d)



	_play_target_voice(null, duck_group_appear_stream)


func _spawn_slider(scene: PackedScene) -> void :
	if scene == null:
		return
	var t: = scene.instantiate() as TargetBase
	targets_root.add_child(t)

	var y_lo: float = _viewport_size.y * 0.55
	var y_hi: float = _viewport_size.y * 0.9
	var y: float = randf_range(y_lo, y_hi)

	var going_right: bool = randf() < 0.5
	var x: float = -30.0 if going_right else _viewport_size.x + 30.0
	t.global_position = Vector2(x, y)
	if t.has_method("set"):
		var speed: float = _current_duck_speed() * (1.0 if going_right else -1.0)
		t.set("speed", speed)
	_hook_target(t)


func _spawn_popup() -> void :
	if popup_scene == null:
		return
	var p: = popup_scene.instantiate() as TargetBase
	targets_root.add_child(p)

	var x: float = randf_range(120.0, _viewport_size.x - 120.0)
	var y: float = randf_range(_viewport_size.y * 0.35, _viewport_size.y * 0.65)
	p.global_position = Vector2(x, y)

	if p.has_method("set"):
		p.set("visible_time", _current_popup_visible_time())
	_hook_target(p)




func _current_duck_interval() -> float:



	return lerp(initial_duck_interval, 1.2, _difficulty_frac())

func _current_duck_speed() -> float:




	return lerp(initial_duck_speed, 700.0, _difficulty_frac())

func _current_civilian_ratio() -> float:


	return lerp(initial_civilian_ratio, 0.44, _difficulty_frac())

func _current_popup_interval() -> float:

	return lerp(initial_popup_interval, 0.8, _difficulty_frac())

func _current_popup_visible_time() -> float:

	return lerp(0.5, 0.18, _difficulty_frac())

func _difficulty_frac() -> float:
	if difficulty_max_steps <= 0:
		return 0.0
	return float(_difficulty) / float(difficulty_max_steps)




func _win() -> void :
	if _ended:
		return
	_ended = true
	_set_ingame_input_mode(false)
	if _music != null:
		_music.stop()
	if _sfx_target_voice != null:
		_sfx_target_voice.stop()
	_play_sfx(_sfx_win)


	var fs: Node = get_tree().root.get_node_or_null("FlagService")
	if fs == null:
		push_error("Gallery: FlagService autoload missing")
		_show_flag_overlay("ERROR_NO_FLAG_SERVICE")
		return
	if not fs.has_method("request_marker"):
		_show_flag_overlay("ERROR_BAD_FLAG_SERVICE")
		return
	fs.call("request_marker", func(result: String) -> void :
		_show_flag_overlay(result)
	)


func _lose() -> void :
	if _ended:
		return
	_ended = true
	_set_ingame_input_mode(false)
	if _music != null:
		_music.stop()
	if _sfx_target_voice != null:
		_sfx_target_voice.stop()
	_play_sfx(_sfx_lose)
	_show_lose_overlay()


func _show_flag_overlay(marker_or_err: String) -> void :
	print("MARKER: ", marker_or_err)
	get_tree().create_timer(1.0).timeout.connect(func(): get_tree().quit())
	if flag_overlay_scene == null:
		push_error("Gallery: flag_overlay_scene not assigned in inspector.")
		print("MARKER: ", marker_or_err)
		return
	var overlay: = flag_overlay_scene.instantiate()
	get_tree().current_scene.call_deferred("add_child", overlay)
	overlay.call_deferred("set_marker", marker_or_err)


func _show_lose_overlay() -> void :
	if lose_overlay_scene == null:
		push_error("Gallery: lose_overlay_scene not assigned in inspector.")
		return
	var overlay: = lose_overlay_scene.instantiate()
	get_tree().current_scene.call_deferred("add_child", overlay)
	if overlay.has_signal("retry_requested"):
		overlay.retry_requested.connect(_on_retry_requested)


func _on_retry_requested() -> void :

	for t in get_tree().get_nodes_in_group("targets"):
		t.queue_free()
	_score = 0
	_time_left = round_seconds
	_elapsed = 0.0
	_difficulty = 0
	_ended = false
	_duck_spawn_timer = 0.3
	_popup_spawn_timer = 1.5
	_voice_owner = null
	hud.set_score(_score)
	hud.set_time(_time_left)

	_flip_wave_index = 0
	_spawn_flip_wave()

	if _music != null and _music.stream != null:
		_music.play()
	_set_ingame_input_mode(true)




func _toggle_help_overlay() -> void :
	if _help_overlay != null and is_instance_valid(_help_overlay):
		return
	if help_overlay_scene == null:
		return
	_help_overlay = help_overlay_scene.instantiate()
	get_tree().current_scene.call_deferred("add_child", _help_overlay)
	if _help_overlay.has_signal("closed"):
		_help_overlay.closed.connect(_on_help_overlay_closed)
	if _help_overlay.has_signal("start_over_requested"):
		_help_overlay.start_over_requested.connect(_on_retry_requested)
	_set_ingame_input_mode(false)


func _on_help_overlay_closed() -> void :
	_help_overlay = null


	if not _ended:
		_set_ingame_input_mode(true)







func _set_ingame_input_mode(ingame: bool) -> void :
	if ingame:
		Input.mouse_mode = Input.MOUSE_MODE_HIDDEN
		if crosshair_root != null:
			crosshair_root.visible = true
	else:
		Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
		if crosshair_root != null:
			crosshair_root.visible = false
