/****************************************************************************
 * Copyright (c) Peter Monks 2010, 2011
 * This work is licensed under a Creative Commons Attribution-ShareAlike
 * 3.0 Unported License.  See http://creativecommons.org/licenses/by-sa/3.0/
 * for full details.
 ****************************************************************************/
@Grab(group="org.apache.commons", module="commons-lang3",  version="3.1")
@Grab(group="org.slf4j",          module="slf4j-api",      version="1.6.4")
@Grab(group="ch.qos.logback",     module="logback-core",   version="1.0.1")
@Grab(group="org.twitter4j",      module="twitter4j-core", version="4.0.6")

import twitter4j.*
import twitter4j.api.*
import org.apache.commons.lang3.StringEscapeUtils

if (args.length == 0)
{
  println "Please provide your query on the command line.  Note: the hash character (#) needs to be escaped on Unix."
  System.exit(-1)
}

def twitter = new TwitterFactory().instance
def query   = new Query(args[0])
def page    = 1  // Note: the Twitter API starts pages #s at 1

query.rpp(100)  // Results per page
query.page(page)

def result     = twitter.search(query)
def numResults = result.tweets.size

// Loop through all pages of tweets
while (page < 1500 &&
       numResults > 0)
{
  // Loop through the current page of tweets, printing each one in an HTML format
  result.tweets.each { tweet ->
    println """  <tr>
    <td><a href="http://www.twitter.com/${tweet.fromUser}">@${StringEscapeUtils.escapeHtml4(tweet.fromUser)}</a><br/>
        <a href="http://www.twitter.com/${tweet.fromUser}/status/${tweet.id}">${String.format('%tF', tweet.createdAt)} ${String.format('%tT', tweet.createdAt)}</a></td>
    <td>${StringEscapeUtils.escapeHtml4(tweet.text)}</td>
    <td></td>
  </tr>"""
  }
  
  page++
  query.page(page)
  result     = twitter.search(query)
  numResults = result.tweets.size
}
