import {State} from './state.js'

export class Map {
    constructor(name, width, height, fields, player_position, crate_positions) {
        this._check_size(width, height, fields)
        this.name = name
        this.width = width
        this.height = height
        this.fields = fields
        this._initial_player_position = player_position
        this._initial_crate_positions = crate_positions
    }

    _check_size(width, height, fields) {
        if (len(fields) !== width * height) {
            throw new ValueError()
        }
    }

    __getitem__(coordinates) {
        if (this._outOfBounds(coordinates.x, coordinates.y)) {
            throw new ValueError()
        }
        return this.fields[y * this.width + x]
    }

    _outOfBounds(x, y) {
        return x < 0 || y < 0 || x >= this.width || y >= this.height
    }

    accessible(x, y) {
        if (x < 0 || y < 0 || x >= this.width || y >= this.height) {
            return false
        } else {
            return this.fields[y * this.width + x].accessible
        }
    }

    create_initial_state() {
        return State(this._initial_player_position, this._initial_crate_positions)
    }
}
