// @flow
import * as React from 'react';
import { Link } from "react-router-dom";
import { Carousel } from 'antd';
import './Library.css';

const DATA = require('../../src/us-top-100-podcasts.json')
const SLIDES_TO_SHOW = 6;

export type Props  = {
    itunes_rss: string;
}
export type Podcast = {
    url: string,
    artistName: string,
    id: string,
    releaseDate: string,
    name: string,
    artworkUrl100: string,
    genres: Array<Genre>
}
export type State = {
    loading: boolean,
    podcasts: Array<any>,
}

class Library extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {
            loading: false,
            podcasts: DATA['feed']['results']
        }
    }

    render() {
        if (this.state.loading) {
            return <span>Loading</span>
        }
        const genres = getPodcastGenres(this.state.podcasts);
        const strips = Object.keys(genres).map((key: string) => 
            <div key={key}><GenreStripCard  name={key} podcasts={genres[key]} /></div>);
        return (
            <div className="library-container">{strips}</div>
        );
    }

}
export default Library;

export function LibraryCard(props: Podcast) {
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

function getpodIdFromUrl(url: string): number {
    let match = url.match(/id(\d+)/)
    let podID: any = null;

    if (match) {
        podID = match[1]; 
    } else {
        podID = url.match(/\d+/);  // 123456 
    } 

    if (!podID) {
        throw "Provided url seems to be invalid";
    }
    return podID
}

interface Genre {
    name:    string;
    podcasts: Array<Podcast>;
}
function getPodcastGenres(podcasts: Array<Podcast>) {
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
        if    (genres[key].length < SLIDES_TO_SHOW) {
            delete genres[key]
        }
    });
    return genres
}

function GenreStripCard(genre: Genre) {
    const cards = genre['podcasts'].map((podcast: Podcast) => 
        <div key={podcast.id} className="item"><LibraryCard  {...podcast} /></div>);
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: SLIDES_TO_SHOW,
        slidesToScroll: Math.ceil(SLIDES_TO_SHOW / 3),
        arrows: true
        };
    return (
        <div className='genre-strip'>
            <h1>{genre.name}</h1>
            <Carousel {...settings}>{cards}</Carousel>
        </div> 
    );
}