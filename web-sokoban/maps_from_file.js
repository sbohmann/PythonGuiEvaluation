import {MapFromLines} from './map_from_lines.js'

export class MapsFromFile {
    constructor(path) {
        this.result = []
        this._current_map_lines = null
        this._read_lines(path)
    }

    _read_lines(path) {
        for (let raw_line of io.open(path)) {
            let line = raw_line.strip("\n\r")
            this._process_line(line)
        }
    }

    _process_line(line) {
        if (this._current_map_lines == null) {
            this._attempt_map_start(line)
        } else {
            this._add_line_to_map(line)
        }
    }

    _attempt_map_start(line) {
        if (line.length !== 0) {
            this._start_new_map(line)
        }
    }

    _start_new_map(line) {
        if (!is_map_line(line)) {
            throw new ValueError('Not a map line: [' + line + ']')
        }
        this._current_map_lines = [line]
    }

    _add_line_to_map(line) {
        if (is_map_line(line)) {
            this._current_map_lines.append(line)
        } else {
            this._processs_end_line(line)
        }
    }

    _processs_end_line(line) {
        let name = this._read_name_from_end_line(line)
        this.result.append(
            MapFromLines(name, this._current_map_lines).result)
        this._current_map_lines = null
    }

    _read_name_from_end_line(line) {
        let match = end_line_pattern.fullmatch(line)
        if (match == null) {
            throw new ValueError('Not an end line: [' + line + ']')
        }
        return match.group(1)
    }
}

const map_line_pattern = re.compile('[# .$*@+]+')
const end_line_pattern = re.compile('; (.*)')

function is_map_line(line) {
    return map_line_pattern.fullmatch(line) !== null
}
