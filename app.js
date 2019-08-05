// A simple echo bot for the Microsoft Bot Framework.

var restify = require('restify');
var builder = require('botbuilder');
var botbuilder_azure = require("botbuilder-azure");

// Setup Rstify Server

var server = restify.createServer();
serverlisten(process.env.port || process.env.PORT || 3978, function(){
  console.log('%s listening to %s', server.name, server.url);
});
