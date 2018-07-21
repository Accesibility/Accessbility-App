'use strict';
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const server = app.listen(5000, () => {
  console.log('Express server listening on port %d in %s mode', server.address().port, app.settings.env);});

app.post('/events', (req, res) => {
  let q = req.body;
  // 1. To see if the request is coming from Slack
  if (q.token !== process.env.SLACK_VERIFICATION_TOKEN) {
    res.sendStatus(400);
    return;
  }
  // 2. Events - get the message text
  else if (q.type === 'event_callback') {
    if(!q.event.text) return;
    analyzeTone(q.event); // sentiment analysis
  }
});
