export class DatabaseMemory {
    #tasks = []

    async create(task) {
        this.#tasks.push(task)
    }

    async update(id, task) {
        this.#tasks.push(task)
    }
}