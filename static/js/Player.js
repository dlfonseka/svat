import ReactPlayer from 'react-player'

function Player({src, playing}) {
    return (
        <div className='player-wrapper'>
            <ReactPlayer 
                url={src}
                config={{
                    file: {forceVideo: true}
                }}
                controls={false}
                width='100%'
                height='100%'
                playing={playing}
                light={true}
                className='react-player'
                />

        </div>
    )
}

export default Player
