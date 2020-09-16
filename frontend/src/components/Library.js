// @flow
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from "react-router-dom";
import { Carousel } from 'antd';
import './Library.css';

const DATA = require('../../src/us-top-100-podcasts.json')
const SLIDES_TO_SHOW = 6;

export type Genre = {
    name: string,
}
export type Podcast = {
    url: string,
    artistName: string,
    id: string,
    releaseDate: string,
    name: string,
    artworkUrl100: string,
    genres: Array<Genre>,
}
export type DenseGenre = {
    name: string,
    podcasts: Array<Podcast>,
}
export type State = {
    loading: boolean,
    podcasts: Array<any>,
}

export const Library = () => {
    const [podcasts, setPodcasts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get(`http://localhost:8000/itunes/`).then(res => {
            setPodcasts(res.data)
            setLoading(false)
        })
    }, [])

    if (loading) {
        return <span>Loading</span>
    }

    const genres = getPodcastGenres(podcasts);
    const strips = Object.keys(genres).map((key: string) => <GenreStripCard name={key} podcasts={genres[key]} key={key} />);    
    return <div className="library-container">{strips}</div>
}

export const LibraryCard = (props: Podcast) => {
    const link = `/podcast/${getpodIdFromUrl(props.url)}`;
    return (
        <Link to={link} >
            <div className="podcast-card">
                <img className="podcast-image" src={props.artworkUrl100} alt={props.name} />
                <div className="podcast-details">
                    <h2>{props.artistName}</h2>
                    <h3>{props.name}</h3>
                </div>
                <div className="clearfix" />
            </div>
        </Link>
    );
}

const getpodIdFromUrl = (url: string): number => {
    let match = url.match(/id(\d+)/)
    if (match) {
        return parseInt(match[1]); 
    } 
    match = url.match(/\d+/); //try less structured match 
    if (match) {
        return parseInt(match[1]); 
    } 
    throw new Error("Provided url seems to be invalid");
}

const getPodcastGenres = (podcasts: Array<Podcast>) => {
    let genres = {};
    podcasts.forEach((podcast) => {
        podcast.genres.forEach((genre: Genre) => {
            if (genre.name === 'Podcasts' || genre.name === 'Podcasting') {
                return
            }
            if (!(genre.name in genres)) {
                genres[genre.name] = [];
            }
            genres[genre.name].push(podcast);
        })
    })

    Object.keys(genres).forEach((key) => {
        if(genres[key].length < SLIDES_TO_SHOW) {
            delete genres[key]
        }
    });
    return genres
}

const GenreStripCard = (genre: DenseGenre) => {
    const cards = genre['podcasts'].map((podcast: Podcast) => 
        <div key={podcast.id} className="item"><LibraryCard  {...podcast} /></div>);
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: SLIDES_TO_SHOW,
        slidesToScroll: Math.ceil(SLIDES_TO_SHOW / 3),
        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                initialSlide: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
        ],
        arrows: true
        };
    return (
        <div className='genre-strip'>
            <h1>{genre.name}</h1>
            <Carousel {...settings}>{cards}</Carousel>
        </div> 
    );
}
