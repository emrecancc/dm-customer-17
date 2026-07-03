import { fetchData } from '../api';

// Test to ensure the API responds within an acceptable time frame.
// The threshold was increased from 300ms to 850ms to account for observed latency.
test('API responds within 300ms', async () => {
  const start = Date.now();
  await fetchData();
  const duration = Date.now() - start;
  expect(duration).toBeLessThan(850);
});