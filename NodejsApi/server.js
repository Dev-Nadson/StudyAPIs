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

server.get('/', () => {
    const tasks = db.list()
    return tasks
})

server.put('/tasks/:id', (req, reply) => {
    const taskID = req.params.id
    const { title, description } = req.body

    db.update(taskID, {
        title: title,
        description: description
    })

    return reply.status(200).send
})

server.delete('/tasks/:id', () => {
    return "Hello World!"
})
server.listen({
    port: 3333,
})