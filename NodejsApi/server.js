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
    const videos = db.list()
    return videos
})

server.put('/tasks/:id', () => {
    return "Hello World!"
})

server.delete('/tasks/:id', () => {
    return "Hello World!"
})
server.listen({
    port: 3333,
})