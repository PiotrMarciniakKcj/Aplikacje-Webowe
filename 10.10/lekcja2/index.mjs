import express from 'express'
import { readFile, writeFile } from 'fs/promises'
const app = express()
const port = 3000

app.get('/', async (req,res) => {
  const html = await readFile('home.html')
  res.send(html)
})

app.post('/kontakt', async (req,res) => {

})

app.listen(port, () => {
  console.log(`server listening at port ${port}`)
})

/*tez podjebane od wojtka i tez przeanalizowane */