class State {
    __init__(map, player_position, crate_positions) {
        this._map = map
        this._player_position = player_position
        this._crate_positions = set(crate_positions)
    }

    get player_position() {
        return this._player_position
    }

    get crate_positions() {
        return this._crate_positions
    }

    move(dx, dy) {
        let new_x = this._player_position + dx
        let new_y = this._player_position + dy
        if ((!this._map.accessible(new_x, new_y))) {
            return false
        }
        if ((!this._clear_path(new_x, new_y, dx, dy))) {
            return false
        }
        this._player_position = position(new_x, new_y)
        return true
    }

    _clear_path(x, y, dx, dy) {
        if (position(x, y) in this._crate_positions) {
            return this._move_crate(x, y, dx, dy)
        } else {
            return true
        }
    }

    _move_crate(crate_x, crate_y, dx, dy) {
        let previous_crate_position = position(crate_x, crate_y)
        this._check_crate_position(previous_crate_position)
        let new_crate_position = position(crate_x + dx, crate_y + dy)
        return this._move_crate_if_possible(previous_crate_position, new_crate_position)
    }

    _move_crate_if_possible(previous_crate_position, new_crate_position) {
        if (this._position_accessible_for_crate(new_crate_position)) {
            this._replace_crate_position(previous_crate_position, new_crate_position)
            return true
        } else {
            return false
        }
    }

    _replace_crate_position(previous_crate_position, new_crate_position) {
        this._crate_positions.remove(previous_crate_position)
        this._crate_positions.add(new_crate_position)
    }

    _position_accessible_for_crate(position) {
        return this._map.accessible(position.x, position.y) &&
            !this._crate_positions.contains(position)
    }

    _check_crate_position(position) {
        if (!this._crate_positions.contains(position)) {
            throw new ValueError()
        }
    }
}

function position(x, y) {
    return {x: x, y: y}
}
