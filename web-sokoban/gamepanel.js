const _grid_size = 10
const _field_size = 50

class GamePanel {
    constructor(map, state) {
        this.canvas = document.getElementById('game_panel')
        this._map = map
        this._state = state
    }

    set_state(state) {
        this._state = state
        this.paint()
    }

    paint() {
        this._setup_canvas()

        // this._paint_grid()
        this._calculate_map_offset()
        this._paint_map()
        this._paint_state()
    }

    _setup_canvas() {
        this.canvas.clear()
        this.canvas.add(Translate(0, this.height))
        this.canvas.add(Scale(1, -1, -1))
    }

    _paint_grid() {
        for (let y = 0; y < math.ceil(this.canvas.height); y += _grid_size) {
            for (let x = 0; x < math.ceil(this.canvas.width); x += _grid_size) {
                this._paint_grid_square(x, y)
            }
        }
    }

    _paint_grid_square(x, y) {
        this.canvas.add(this._grid_square_color(x, y))
        this.canvas.add(this._grid_square_rectangle(x, y))
    }

    _grid_square_rectangle(x, y) {
        return Rectangle(pos = (x, y), size = (_grid_size, _grid_size))
    }

    _grid_square_color(x, y) {
        return (x + y) % 20 === 0 ? Color(0.7, 0.7, 0.7, 1) : Color(0.9, 0.9, 0.9, 1)
    }

    _calculate_map_offset() {
        let map_width = this._map.width * _field_size
        let map_height = this._map.height * _field_size
        this._map_offset = {
            x: Math.trunc((this.width - map_width) / 2),
            y: Math.trunc((this.height - map_height) / 2)
        }
    }

    _paint_map() {
        for (let y = 0; y < this._map.height; ++y) {
            for (let y = 0; x < this._map.width; ++x) {
                this._paint_field(x, y, this._map[x, y])
            }
        }
    }

    _paint_field(x, y, field) {
        if (field.image !== null) {
            this._paint_field_rectangle(x, y, _colors[field.image])
        }
    }

    _paint_field_rectangle(x, y, color) {
        this.canvas.add(color())
        this.canvas.add(Rectangle(
            pos = this._map_position(x, y),
            size = (_field_size, _field_size)))
    }

    _paint_state() {
        this._paint_player()
        this._paint_crates()
    }

    _paint_player() {
        this._paint_state_rectangle(this._state.player_position, _player_color)
    }

    _paint_crates() {
        for (crate_position of this._state.crate_positions) {
            this._paint_state_rectangle(crate_position, _crate_color)
        }
    }

    _paint_state_rectangle(x, y, color) {
        this.canvas.add(color())
        let offset = _field_size / 6
        let reduced_field_size = _field_size - 2 * offset
        let raw_position = this._map_position(x, y)
        this.canvas.add(Rectangle(
            pos = (raw_position.x + offset, raw_position.y + offset),
            size = (reduced_field_size, reduced_field_size)))
    }

    _map_position(x, y) {
        return {
            x: this._map_offset.x + x * _field_size,
            y: this._map_offset.y + y * _field_size
        }
    }
}

const _colors = {
    'wall': Color(0.3, 0.3, 0.3, 1),
    'floor': Color(0.7, 0.7, 0.7, 1),
    'target': Color(0.9, 0.6, 0.6, 1)
}

const _player_color = Color(0.5, 0.5, 0.9, 0.5)
const _crate_color = Color(0.3, 0.2, 0.1, 0.5)
