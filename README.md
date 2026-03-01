# biomed-data-analyzer
CS50P final project
    # ECG curve analyzer for final project CS50P
    #### Video Demo:  https://youtu.be/InoyROAg8Tk
    #### Description:
    # Introduction
    As a future biomedical engineer, I chose this topic to learn and discover how to work with biosignals, their processing, and subsequent display.
    My final project deals with reading and processing ECG signals and subsequent detection of R peaks to determine BPM (beats per minute).

    # Usage
    The program works on the principle that the user launches the signal and enters the name of the file they want to open, after which the subsequent data for the ECG curve is taken from the website https://www.kaggle.com/datasets/protobioengineering/mit-bih-arrhythmia-database-modern-2023/data.

    # Summary of functions
    ## load_data
        In the first part of the load_file function, I use the pandas library to load data from a CSV file containing ECG curve data and select the column with MLII data, which represents the ECG curve. In this function, I also check whether the file exists and whether it contains any data.
    ## peaks_detection
        In the peaks_detection function, we implement the findpeaks function from the scipy library for processing, which searches for local signal maxima, i.e., our R peak. This useful function carries with it a detection height parameter, which was set at 70% of the signal as my threshold value, and a distance between peaks of 150 samples. This setting was not necessary because the signal was well filtered and the R peaks were clearly visible, probably due to signal normalization. We then also calculated the number of detected peaks.
    ## calculate_bpm,diagnose_bpm
        We also have the calculate_bpm and diagnose_bpm functions, which correlate with each other. In the function for calculating BPM, I had to convert the number of signal samples to time. I did this by using the len function to find the number of signal samples and dividing it by the sampling frequency, which tells us how many samples were taken every second. I then used a simple formula to calculate BPM. which is not very complicated to explain: we simply divide the total number of detected peaks by the total signal time and multiply by 60.
        The function for diagnosing these metrics then tells us the patient's condition based on physiological assumptions, where it is divided into three phases: normal, which is 60 to 100 BPM; below 60 is bradycardia; and above is tachycardia.
    ## grapg
        The graphical display is used for visualization and also for subjective control of whether the R peak was detected correctly, using the matplotlib library, where we had to calculate the time , where we calculated the time by indexing the signal and dividing it by the sampling frequency, and we did the same for the detected peaks. We then created one graph with the original signal and another with points that overlapped the detected R peaks using red crosses. We gave it axes and a title, displayed the graph, and saved it.
    ## rr_intervals and main
        The penultimate part is a simple function where, with the help of the numpy library, we subtract two adjacent R peaks to determine heart rate variability, and then in the main function, we call all these functions and work with them.
    ## test_project.py
        In the test_project.py file, I tested three functions: whether the bpm is calculated correctly if the diagnosis is correctly determined based on physiological assumptions, and whether the peaks are correctly detected to verify the find_peaks function.

