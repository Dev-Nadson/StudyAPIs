import { randomUUID } from 'node:crypto'
import sql from './db.js'

export class DatabasePostgres {
    async list(search) {
        let tasks
        if (search) {
            tasks = await sql`select * from tasks where title ilike ${'%' + search + '%'}` //ilike considera de todas as formas, seja maiusculo, minusculo, etc
        } else {
            tasks = await sql`select * from tasks`
        }
        return tasks
    }
    async create(task) {
        const taskID = randomUUID()
        const { title, description } = task

        await sql`insert into tasks (id, title, description) VALUES (${taskID}, ${title}, ${description})`
    }
    async update(id, task) {
        const { title, description } = task

        await sql`update tasks set title = ${title}, description = ${description} WHERE id = ${id}`
    }
    async delete(id) {
        await sql`delete from tasks WHERE id = ${id}`

    }
}