import { spawn } from 'child_process';

export default async (req, res) => {
  try {
    const pyprog = spawn('python', ['../.././python/app.py']);
    
    pyprog.stdout.on('data', (data) => {
      res.status(200).json({ result: data.toString() });
    });
    
    pyprog.stderr.on('data', (data) => {
      res.status(500).json({ error: data.toString() });
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};
