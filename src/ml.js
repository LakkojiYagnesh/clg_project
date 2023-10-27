const { exec } = require('child_process');

function run(txt) {
  return new Promise((resolve, reject) => {
    exec(`python sentilyzer.py "${txt}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing Python script: ${error}`);
        reject(error);
      } else {
        resolve(stdout.trim());
      }
    });
  });
}


//const testText = "College management is not good";
module.exports = {run};