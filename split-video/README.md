# split-video

## Description
This script splits a video file into a specified number of equal-duration parts using FFmpeg. It automatically calculates the duration of each part and handles any remaining seconds by adding them to the last part.

## Requirements
- Bash
- FFmpeg (with `ffprobe` and `ffmpeg` commands)
- Input video file

## Usage
```bash
bash split_video.sh <video_file> <number_of_parts>
```

### Parameters
- `video_file`: Path to the input video file
- `number_of_parts`: Number of parts to split the video into

### Example
```bash
bash split_video.sh movie.mp4 3
bash split_video.sh /path/to/video.avi 5
```

## What it does
1. **Duration Detection**: Uses `ffprobe` to get the total duration of the video
2. **Part Calculation**: Calculates the duration for each part (total_duration / number_of_parts)
3. **Remainder Handling**: Adds any remaining seconds to the last part
4. **Video Splitting**: Uses `ffmpeg` to create each part with precise timing
5. **File Naming**: Creates output files with sequential numbering

## Output Files
For a video named `movie.mp4` split into 3 parts:
```
movie_part1.mp4
movie_part2.mp4
movie_part3.mp4
```

## Example Output
```bash
$ bash split_video.sh movie.mp4 3
Total duration: 150 seconds
Duration per part: 50 seconds
Remainder: 0 seconds
Creating part 1: 0 to 50 seconds
Creating part 2: 50 to 100 seconds
Creating part 3: 100 to 150 seconds
Video splitting completed!
```

## Features
- **Automatic Duration Calculation**: No need to manually calculate timings
- **Precise Splitting**: Uses exact timestamps for clean cuts
- **Remainder Handling**: Ensures no content is lost by adding extra seconds to the last part
- **Progress Feedback**: Shows the creation of each part
- **Flexible Input**: Works with various video formats supported by FFmpeg
- **Sequential Naming**: Creates clearly numbered output files

## Use Cases
- **File Size Management**: Breaking large videos into smaller, manageable parts
- **Upload Preparation**: Creating parts that fit platform size limits
- **Content Distribution**: Splitting content for easier sharing
- **Storage Optimization**: Distributing video across multiple storage locations
- **Streaming Preparation**: Creating segments for streaming applications
- **Backup Strategy**: Creating multiple backup parts

## Technical Details
- Uses `ffprobe` to extract video metadata
- Employs `ffmpeg` with `-c copy` for fast, lossless splitting
- Handles integer division remainders automatically
- Preserves original video quality and format
- Uses precise timestamp formatting (HH:MM:SS)

## Error Handling
The script includes basic validation:
- Checks for correct number of arguments
- Verifies video file existence
- Validates FFmpeg installation