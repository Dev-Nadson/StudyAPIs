/*import { fastify } from 'fastify'
import { DatabasePostgres } from './database-postgres.js'

const server = fastify()
const db = new DatabasePostgres()

server.post('/tasks', async (req, reply) => {
    const { title, description } = req.body

    await db.create({
        title: title,
        description: description
    })

    return reply.status(201).send()
})

server.get('/', async (req) => {
    const search = req.query.search

    console.log(search)
    const tasks = await db.list(search)
    return tasks
})

server.put('/tasks/:id', async (req, reply) => {
    const taskID = req.params.id
    const { title, description } = req.body

    await db.update(taskID, {
        title: title,
        description: description
    })

    return reply.send()
})

server.delete('/tasks/:id', async (req, reply) => {
    const taskID = req.params.id
    await db.delete(taskID)

    return reply.status(204).send()
})
server.listen({
    port: 3333,
})*/

import { buildApp } from './app.js'

const app = await buildApp()

app.listen({ port: 3333 }, (err, address) => {
    if (err) {
        console.error(err)
        process.exit(1)
    }
    console.log(`🚀 Servidor rodando em ${address}`)
})

