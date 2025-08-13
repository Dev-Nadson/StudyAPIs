import { fastify } from 'fastify'

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