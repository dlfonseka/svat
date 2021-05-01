import Button from './Button'

function Header() {
    return (
        <header className='header'>
            <h2 style={{'display':'inline', 'vertical-align':'middle'}}>Surgical Video Annotation Tool</h2>
            <button type='button' id='topbtn'>
                <img src='../media/download.png' style={{'vertical-align':'middle'}}/>
                <span>Download Data</span>
            </button>

            <button type='button' id='topbtn'>
                <img src='../media/upload.png' style={{'vertical-align':'middle'}}/>
                <span>Upload Annotations</span>
            </button>

            <button type='button' id='topbtn'>
                <img src='../media/plus.png' style={{'vertical-align':'middle'}}/>
                <span>Download Annotations</span>
            </button>


        </header>
    )
}

export default Header
