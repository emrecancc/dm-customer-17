import { server } from '../src/server';

beforeAll(() => {
  server.listen(3019);
});

// Existing tests

test('example', () => {
  // test logic
});

// Ensure the server is closed after all tests to avoid port conflicts
afterAll(() => {
  server.close();
});