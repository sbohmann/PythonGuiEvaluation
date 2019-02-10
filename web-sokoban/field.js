export class Field {
    constructor(key) {
        this.visible = (key !== null)
        if (key === null) {
            this.accessible = false
            this.target = false
            this.image = null
        } else if (key === '#') {
            this.accessible = false
            this.target = false
            this.image = 'wall'
        } else if (key === ' ' || key === '$' || key === '@') {
            this.accessible = true
            this.target = false
            this.image = 'floor'
        } else if (key === '.' || key === '*' || key === '+') {
            this.accessible = true
            this.target = true
            this.image = 'target'
        }
    }
}
