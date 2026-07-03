const server = require('../server');
const request = require('supertest');

let app;

beforeAll(() => {
  app = server.listen(0);
});

afterAll(() => {
  app.close();
});

test('GET /', async () => {
  const res = await request(app).get('/');
  expect(res.statusCode).toBe(200);
});