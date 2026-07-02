import React from 'react';
import { render } from '@testing-library/react';
import Dashboard from '../Dashboard';

test('Dashboard renders correctly', () => {
  const { container } = render(<Dashboard />);
  expect(container).toMatchSnapshot({ maxDiff: 1000 });
});