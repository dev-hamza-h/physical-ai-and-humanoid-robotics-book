import React from 'react';
import { render, screen } from '@testing-library/react';
import HomepageFeatures from './index';

test('renders features', () => {
  render(<HomepageFeatures />);
  const featureList = screen.getAllByRole('listitem');
  expect(featureList.length).toBe(3);
});
