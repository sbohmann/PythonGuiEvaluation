import {GamePanel} from './gamepanel.js'
import {MapsFromFile} from './maps_from_file.js'

class Sokoban {
    constructor() {
        this._read_maps()
        this._setup_ui()
        this._set_map_index(0)
    }

    build() {
        return this._mainPanel.view
    }

    _setup_state() {
        this._state = this._map.create_initial_state()
    }

    _read_maps() {
        this._maps = MapsFromFile('100Boxes.txt').result
    }

    _setup_ui() {
        this._mainPanel = MainPanel()
        this.setup_keyboard_handling()
    }

    setup_keyboard_handling() {
        this._keyboard = Window.request_keyboard(this._keyboard_closed, this._mainPanel)
        this._keyboard.bind(on_key_down=this._on_keyboard_down)
    }

    _keyboard_closed() {
        this._keyboard.unbind(on_key_down=this._on_keyboard_down)
        this._keyboard = null
    }

    _on_keyboard_down(keyboard, keycode, text, modifiers) {
        console.log(keycode)
        let direction = _direction_for_keycode.get(keycode[1], null)
        if ((direction !== null)) {
            this._move(direction)
        } else if ((keycode[1] === 'escape')) {
            this._reset_state()
        } else if ((keycode[1] === 'pageup')) {
            this._switch_map(1)
        } else if ((keycode[1] === 'pagedown')) {
            this._switch_map(-1)
        }
        return true
    }

    _reset_state() {
        this._state = this._map.create_initial_state()
        this._game_panel.set_state(this._state)
    }

    _move(direction) {
        if (this._state.move(direction.x, direction.y)) {
            this._game_panel.paint()
    }
    }

    _switch_map(delta) {
        let new_map_index = (this._map_index + delta) % len(this._maps)
        if (new_map_index < 0) {
            new_map_index += len(this._maps)
    }
        this._set_map_index(new_map_index)
    }

    _set_map_index(value) {
        this._map_index = value
        this._map = this._maps[this._map_index]
        this._state = this._map.create_initial_state()
        this._game_panel = GamePanel(this._map, this._state)
        this._mainPanel.set_game_panel(this._game_panel)
        this._set_window_title()
    }

    _set_window_title() {
        this.title = 'Sokobal Level ' + str(this._map_index + 1)
    }
}

function _move(position, dx, dy) {
    return position(position.x + dx, position.y + dy)
}

let _direction_for_keycode = {
    'left': direction(-1, 0),
    'right': direction(1, 0),
    'up': direction(0, -1),
    'down': direction(0, 1)
}

function direction(x, y) {
    return {x: x, y: y}
}

new Sokoban().run()
