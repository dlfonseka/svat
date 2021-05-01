//import './App.css';
import Header from './components/Header.js'
import Player from './components/Player.js'
import AddAnnotation from './components/AddAnnotation.js'
import Sidebar from './components/Sidebar.js'
import {useState} from 'react'

//NOTE: for now, the video is stored in the media folder
import video from './media/video.mp4'



function App() {

  const toolchoice = [
    {value: 'Scalpel', name: 'Scalpel'},
    {value: 'Dilators', name: 'Dilators'},
    {value: 'Suction Tip', name: 'Suction Tip'},
    {value: 'Forceps', name: 'Forceps'}
  ]

  const [log, setLog] = useState([])

  const addLogEntry = (logentry) => {
    const id = Math.floor.apply(Math.random() * 10000) + 1
    const newEntry = {id, ...logentry}
    setLog([...log, newEntry])
  }

  const [pausePressed, setPausePressed] = useState(false)


  return (
    <div className="App">
      <div className='row'>
        <Header />
      </div>
      <div className='row'> 
        <div className='wide-column'>
          <Player src={video} playing={!pausePressed}/>
        </div>
        <div className='thin-column'>
          <Sidebar log={log}/>
        </div>
      </div>
      <div className='row'> 
        <div className='annotation-bar'>
          <AddAnnotation choices={toolchoice} onAdd={addLogEntry} 
            pausePressed={pausePressed} setPausePressed={setPausePressed}/>
        </div>
      </div>
    </div>
  );
}

// export default App;
const domContainer = document.querySelector('#annotation-app');
ReactDOM.render(e(App), domContainer)