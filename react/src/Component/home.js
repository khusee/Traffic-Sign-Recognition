import React from 'react'
import './home.css'
const Home = ({fileSelectedHandler,Selectedfile, previewImage,fileUploadHandler,PredictedSign}) =>{
    return(
        <div className='home'>
            <h2>Traffic Sign Classification</h2>
            <div className='image'>
                <div className='uploadedimage'>
                    <img className='img' src={previewImage} alt=''/>
                    <div className='btns'>
                        <input className='input' type='file' onChange={fileSelectedHandler}/>
                        <button className='btn' onClick={fileUploadHandler}>Predict</button>
                    </div>
                     <div className='result'>
                       <span>{PredictedSign}</span>
                     </div>
                </div>
            </div>
        </div>
    );
}

export default Home