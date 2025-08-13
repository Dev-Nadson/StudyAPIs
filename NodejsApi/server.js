import { fastify } from 'fastify'
import { DatabaseMemory } from './database-memory.js'
const server = fastify()

server.post('/tasks', () => {
    return "Hello World!"
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