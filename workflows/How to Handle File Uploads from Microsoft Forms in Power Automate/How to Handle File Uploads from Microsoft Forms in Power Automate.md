---

## How the Flow Works

The automation is divided into **8 simple steps**.

Each step prepares the data needed for the next one until all uploaded files are sent as email attachments.

---

## 1. Receive the Form Response

When someone submits the Microsoft Form, the Power Automate flow starts automatically.

The **Get response details** action then retrieves every answer submitted by the user.

**Input**

```text
Name
National ID
Phone Number
File Upload
```

**Output**

```text
All form responses
```

---

## 2. Organize the Uploaded Files

> **Image path (if this article is inside `articles/medium`)**
>
> `../../images/github/json.png`

<p align="center">
  <img src="../../images/github/json.png" alt="Organizing uploaded files" width="900">
</p>

Files uploaded through Microsoft Forms are **not returned as email attachments**.

Instead, Forms returns a text value containing information about each uploaded file.

The first step is to organize those file references into a single collection.

**Example**

```json
[
  {
    "Type": "Document A",
    "Response": "..."
  },
  {
    "Type": "Document B",
    "Response": "..."
  }
]
```

**Goal**

Create a single collection so every uploaded document can be processed using the same logic.

---

## 3. Parse the JSON

Next, use the **Parse JSON** action.

This converts the text returned by Microsoft Forms into an object that Power Automate can work with.

After parsing, you can access information such as:

* File name
* File identifier (ID)
* File path

---

## 4. Process Each File

Since a form may contain multiple uploaded files, Power Automate processes them one by one using an **Apply to each** loop.

Inside the loop, three operations are performed:

* Check whether a file exists;
* Retrieve the file identifier;
* Generate the attachment name.

Example:

```text
Document A.pdf
Document B.png
Document C.jpg
```

---

## 5. Retrieve the File

At this point, the flow only knows **where the file is stored**.

The **Get file content** action downloads the actual file into the flow.

**Input**

```text
File ID
```

**Output**

```text
Complete file content
```

---

## 6. Build the Attachment Collection

Each downloaded file is added to an array variable.

This collection will later be used by Outlook when sending the email.

```json
{
  "Name": "Document.pdf",
  "ContentBytes": "..."
}
```

When the loop finishes, the array contains every file uploaded through Microsoft Forms.

---

## 7. Prepare the Attachments

Before sending the email, use **Parse JSON** one more time.

This ensures Outlook recognizes the attachment collection in the expected format.

---

## 8. Send the Email

Finally, add the **Send an email (V2)** action.

In the **Attachments** field, use the attachment collection created in the previous steps.

Outlook will automatically include every uploaded document.

<p align="center">
  <img src="../../images/github/e-mail.png" alt="Email with attachments" width="900">
</p>

---

## Result

The recipient receives a single email containing:

* All Microsoft Forms responses;
* Every uploaded document;
* Automatically organized attachments ready for review.
