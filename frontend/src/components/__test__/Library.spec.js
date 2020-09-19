import React from 'react';
import ReactDOM from 'react-dom';
import { render, fireEvent, waitFor, screen } from '@testing-library/react'
import { rest } from 'msw'
import { setupServer } from 'msw/node'
import { MemoryRouter } from "react-router-dom";

import { Library } from '../Library';

const EXPECTED_JSON = [
  {
    'name': 'A Podcast',
    'id': 1,
    'url': 'http://foobar.com/1/',
    'kind': 'podcast',
    'artistName': 'Bob',
    'releaseDate': '2019-12-04',
    'artworkUrl100': 'http://foobar.com',
    'genres': [
        {
            'genreId': 1,
            'name': 'Comedy',
            'url': 'http://foobar.com/1/'
        }
    ]
  }
];

const server = setupServer(
    rest.get('/itunes', (req, res, ctx) => {
      return res(
        ctx.status(200),
        ctx.json(EXPECTED_JSON),
      )
    })
  )

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

test('loads and displays podcasts', async () => {
    render(<MemoryRouter><Library /></MemoryRouter>)
    await waitFor(() => screen.getAllByText('A Podcast'))
    expect(screen.getAllByText('A Podcast')[0].tagName.toLowerCase() === 'h2');
  })