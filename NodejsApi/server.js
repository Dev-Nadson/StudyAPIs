import { fastify } from 'fastify'
import { DatabaseMemory } from './database-memory.js'

const server = fastify()
const db = new DatabaseMemory()

server.post('/tasks', (req, reply) => {
    db.create({
        title: 'Corrigir bugs',
        description: 'Corrigir bugs na aplicação'
    })

    return reply.status(201).send()
})

server.get('/', () => {
    return "Hello World!"
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