import { randomUUID } from 'node:crypto'

export class DatabaseMemory {
    #tasks = new Map() //Map para poder fazer a conexão entre ID e Tarefa

    async list() {
        return this.#tasks.values()
    }

    async create(task) {
        const taskID = randomUUID
        this.#tasks.set(taskID, task)
    }

    async update(id, task) {
        this.#tasks.set(id, task)
    }

    async delete(id) {
        this.#tasks.delete(id)
    }
}