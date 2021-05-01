import {useState} from 'react'
import Button from './Button.js'


function AddAnnotation({choices, onAdd, pausePressed, setPausePressed}) {

    const [tool, setTool] = useState('')
    const [detail, setDetail] = useState('')


    const onSubmit = (e) => {
        e.preventDefault()
        // if (!tool) {
        //     alert('Add tool')
        //     return
        // }
        onAdd({tool, detail})
        setTool('')
        setDetail('')
    }
    
    return (
        <form className='add-annotation' onSubmit={onSubmit}>

            <Button    
                onClick={() => setPausePressed(!pausePressed)}
                color={!pausePressed ? '#ffb3b3' : '#e6ffe6'}
                text={!pausePressed ? 'Pause Video' : 'Save Annotation'}
                id='annotate'
                type={pausePressed ? 'button' : 'submit'}/>
            {pausePressed && <div className='dropdown-container'>
                {/* <label for='tools'></label> */}
                <select className='dropdown' onChange={(e) => setTool(e.target.value)}>
                    <option value='' selected disabled>Select Tool</option>
                    {choices.map((e, key) => {
                            return <option key={key} value={e.value}>{e.name}</option>})
                    }
                </select>
            </div>}
            {pausePressed && <div className='form-control' style={{display:'inline'}}>
                <input className='textbox' style={{display:'inline'}} type='text' placeholder={'Detail'} 
                    onChange={(e) => setDetail(e.target.value)}/>
            </div>}
        </form>
    )
}

export default AddAnnotation
