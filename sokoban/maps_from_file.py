import re
import io

from map_from_lines import MapFromLines


class MapsFromFile:
    def __init__(self, path):
        self.result = []
        self._current_map_lines = None
        self._read_lines(path)

    def _read_lines(self, path):
        for raw_line in io.open(path):
            line = raw_line.strip("\n\r")
            self._process_line(line)

    def _process_line(self, line):
        if self._current_map_lines == None:
            self._attempt_map_start(line)
        else:
            self._add_line_to_map(line)

    def _attempt_map_start(self, line):
        if len(line) != 0:
            self._start_new_map(line)

    def _start_new_map(self, line):
        if not is_map_line(line):
            raise ValueError('Not a map line: [' + line + ']')
        self._current_map_lines = [line]

    def _add_line_to_map(self, line):
        if is_map_line(line):
            self._current_map_lines.append(line)
        else:
            self._processs_end_line(line)

    def _processs_end_line(self, line):
        name = self._read_name_from_end_line(line)
        self.result.append(
            MapFromLines(name, self._current_map_lines).result)
        self._current_map_lines = None

    def _read_name_from_end_line(self, line):
        match = end_line_pattern.fullmatch(line)
        if match == None:
            raise ValueError('Not an end line: [' + line + ']')
        return match.group(1)


map_line_pattern = re.compile(' *#(?:[# .$*@+]*#)?')
end_line_pattern = re.compile('; (.*)')


def is_map_line(line):
    return map_line_pattern.fullmatch(line) != None
