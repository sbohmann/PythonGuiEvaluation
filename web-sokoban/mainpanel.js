class MainPanel {
    constructor() {
        this._game_panel = null
        this._create_view()
        this._init_view()
    }

    set_game_panel(_game_panel) {
        this._remove_existing_game_panel()
        this._game_panel = _game_panel
        this.view.add_widget(this._game_panel)
    }

    _remove_existing_game_panel() {
        if (this._game_panel) {
            this.view.remove_widget(this._game_panel)
        }
    }

    _create_view() {
        this.view = GridLayout()
    }

    _init_view() {
        this.view.rows = 1
        this.view.cols = 1
    }
}
