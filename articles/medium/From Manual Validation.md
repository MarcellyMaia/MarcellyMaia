# From Manual Validation to Automation: The Lesson I Learned from Standing in Line

> *Sometimes a process isn't slow because people work slowly. It's slow because it was designed to waste time.*

---

## Introduction

Have you ever stood in a line that just wouldn't move?

It doesn't matter whether it's at a bank, an airport, or a supermarket.

The feeling is always the same.

You look ahead and think,

*"There aren't that many people... so why is this taking so long?"*

Most of the time, the problem isn't the number of people.

It's the process.

While one person searches for a document...

everyone else waits.

While someone switches between screens...

the line gets a little longer.

Minute by minute.

Without anyone noticing.

That was exactly the feeling I had while observing a document validation process.

There wasn't a physical line.

But there was definitely a queue.

A queue of requests waiting to be reviewed.

---

## The Turning Point

At first glance, everything looked modern.

Documents were submitted through Microsoft Forms.

Information was organized.

The process was already digital.

But once I started following the workflow, I noticed something.

To review a single request, someone had to:

Open the form.

Find the correct response.

Open each attachment.

Compare the information.

Go back.

Open the next request.

Repeat.

Microsoft Forms was doing exactly what it was supposed to do.

Collect information.

The real problem started after that.

That's when I asked myself a different question.

> **What if, instead of making it easier to submit documents, I made it easier to review them?**

That simple question changed the entire project.

Using Power Automate, I built a workflow that collected every response, processed the attachments and delivered everything in a single, organized email.

Instead of searching for information...

people received it ready to use.

It sounds like a small improvement.

But small improvements repeated hundreds of times create a huge impact.

---

## The Challenge

The idea was simple.

The implementation wasn't.

Handling file uploads from Microsoft Forms required understanding the JSON structure, retrieving the correct files from Microsoft 365 and refining the flow until it worked consistently.

There were plenty of failed attempts.

Unexpected errors.

And more debugging than I had anticipated.

Looking back, that was probably the part that taught me the most about Power Automate.

---

## The Result

The average review time dropped from around **30 minutes to approximately 10 minutes** per request.

But that wasn't the biggest achievement.

The biggest lesson was realizing that the problem had never been Microsoft Forms.

It wasn't the people.

It wasn't even the business process.

It was the dozens of tiny tasks nobody questioned.

Open another screen.

Click another link.

Search for another file.

Individually, they seemed insignificant.

Together, they consumed hours every single day.

---

## Final Thoughts

Since this project, I've started looking at automation differently.

I no longer search for processes that can be automated.

I look for moments where people are wasting time.

Because that's usually where the greatest opportunities for improvement are hiding.

In this article, I shared the story behind the solution.

If you're curious about the technical implementation, you'll find the complete project, architecture and workflow on my GitHub.

You might even discover that your next automation opportunity is already right in front of you.


### Connect with me

<table>
  <tr>
    <td>
      <a href="https://www.linkedin.com/in/marcelly-maia/">
        <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://medium.com/@cecellymaia4">
        <img src="https://img.shields.io/badge/Medium-Read%20Articles-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium"/>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/MarcellyMaia/MarcellyMaia">
        <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="mailto:marcellygsm@outlook.com">
        <img src="https://img.shields.io/badge/Email-Get%20in%20Touch-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
      </a>
    </td>
  </tr>
</table>


If you enjoyed this article, consider giving this repository a **Star**.

