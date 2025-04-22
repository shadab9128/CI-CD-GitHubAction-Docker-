const request = require('supertest');
const app = require('../app');

describe('GET /', () => {
  it('responds with Hello message', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toContain('Hello from our CI/CD Pipeline!');
  });
});

describe('GET /health', () => {
  it('responds with health status', async () => {
    const response = await request(app).get('/health');
    expect(response.statusCode).toBe(200);
    expect(response.body.status).toBe('healthy');
  });
});