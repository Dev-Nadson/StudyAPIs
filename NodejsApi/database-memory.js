import { randomUUID } from 'node:crypto'

export class DatabaseMemory {
    #tasks = new Map() //Map para poder fazer a conexão entre ID e Tarefa

    async list(search) {
        return Array.from(this.#tasks.entries())
            .map((TaskArray) => {
                const id = TaskArray[0]
                const data = TaskArray[1]

                return {
                    id,
                    ...data
                }
            })
            .filter(task => {
                if (search) {
                    return task.title.includes(search)
                }
                return true
            })
    }

    async create(task) {
        const taskID = randomUUID()
        this.#tasks.set(taskID, task)
    }

    async update(id, task) {
        this.#tasks.set(id, task)
    }
    async delete(id) {
        this.#tasks.delete(id)
    }
}