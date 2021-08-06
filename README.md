# Class balance
DA_alg is a function that will help implement a data augmentation for both EEG sleep and EEG motor recordings in order to adjust the ratio of each present class or label.

For sleep recordings you will have to use :
* ## data_augment_sleep(recording, hypnogram, snr, param)
### Parameters: 

- **recording:** an .edf file of the sleep recording.
  
- **hypnogram:** an .edf file of the sleep hypnogram recording.
  
- **snr:** the requested SNR to be set for the noise, as the data augmentation is based on noise addition.
  
- **param:** can take 3 parameters ('g' for white gaussian noise/	'p' for poisson noise/ 'c' for Chua noise (a chaotic noise)).
### Returns:

- **sleep_stage_1, sleep_stage_2, sleep_stage_3, sleep_stage_4, sleep_stage_rapid_eye_mvt,sleep_stage_wake :** 5 numpy arrays from the 5 sleep stage classes with all arrays having the same length.

---

For motor recordings you will have to use :
* ## data_augment_motor(X, Y, snr, param)
### Parameters: 

- **X:** a numpy array [number_of_channels,time_values] containing the motor recordings.

- **Y:** a numpy array presenting the labels; &#10071; **note that only 3 labels are considered left and right hand movements and others** &#10071;  


- **snr:** the requested SNR to be set for the noise, as the data augmentation is based on noise addition.

- **param:** can take 3 parameters ('g' for white gaussian noise/	'p' for poisson noise/ 'c' for Chua noise (a chaotic noise)).

### Returns:

- **motor_(right\left), motor_(left\right), motor_others :** 3 numpy arrays from the 3 movement classes with all arrays having the same length.
