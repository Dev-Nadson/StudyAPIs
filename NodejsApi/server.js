import { fastify } from 'fastify'
import { DatabaseMemory } from './database-memory.js'

const server = fastify()
const db = new DatabaseMemory()

server.post('/tasks', (req, reply) => {
    const { title, description } = req.body

    db.create({
        title: title,
        description: description
    })

    return reply.status(201).send()
})

server.get('/', (req) => {
    const search = req.query.search

    console.log(search)
    const tasks = db.list(search)
    return tasks
})

server.put('/tasks/:id', (req, reply) => {
    const taskID = req.params.id
    const { title, description } = req.body

    db.update(taskID, {
        title: title,
        description: description
    })

    return reply.send()
})

server.delete('/tasks/:id', (req, reply) => {
    const taskID = req.params.id
    db.delete(taskID)

    return reply.status(204).send()
})
server.listen({
    port: 3333,
})