import {Map} from './map.js'
import {Field} from './field.js'
import {Position} from './state.js'

class MapFromLines {
    constructor(name, lines) {
        this._name = name
        this._lines = lines
        this._player_position = null
        this._crate_positions = []
        this._create_result(name)
    }

    _create_result(name) {
        this._process_lines()
        this._create_fields()
        this.result = Map(name, this._width, this._height,
            this._fields, this._player_position, this._crate_positions)
    }

    _process_lines() {
        this._width = max(map(len, this._lines))
        this._height = len(this._lines)
        this._keys = [null] * this._width * this._height
        for (line, offset in zip(this._lines, range(0, this._height)) {
            this._parse_line(line, offset)
        }
    }

    _parse_line(line, y) {
        let offset = y * this._width
        let started = false
        for (key, x in zip(line, itertools.count())) {
            if (started || key !== ' ') {
                let filtered_key = this._filter_key(key, y)
                this._keys[offset + x] = filtered_key
                started = true
            }
            this._process_key(x, y, key)
        }
    }

    _filter_key(key, y) {
        let outside = this._first_or_last_line(y) && key === ' '
        return outside ? null : key
    }

    _first_or_last_line(y) {
        let first_line = (y === 0)
        let last_line = (y === len(this._lines) - 1)
        return first_line || last_line
    }

    _process_key(x, y, key) {
        if (key === '@' || key === '+') {
            this._set_player_position(x, y)
        } else if (key === '$' || key === '*') {
            this._crate_positions.append(position(x, y))
        }
    }

    _set_player_position(x, y) {
        if (this._player_position != null) {
            throw new ValueError('Double player position')
        }
        this._player_position = position(x, y)
    }

    _create_fields() {
        this._fields = list(map(Field, this._keys))
    }
}
