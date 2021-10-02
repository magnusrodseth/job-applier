# Job Applier 📝

## Description ✏️

This project was created to streamline the process of applying for summer internships.

## Developer Information 🙋🏼‍♂️

Developed by Magnus Rødseth, Autumn 2021.

## Tech Stack 🛠

- Python
- Weasyprint (HTML -> PDF)

## Writing the cover letter outline ✏️

The cover letter outline must be written in Markdown (`.md` extension).

Wherever you would use a company name, you replace it with `{}`. _Why, you ask?_ The script uses string formatting in Python to insert the company name wherever you put `{}` in your cover letter outline.

**This comes with a big caveat!** Python has no functionality that supports inserting 1 string parameter to fill all `{}`'s in the cover letter outline. Hence, we need a workaround. To explain, let's look at an example. Your cover letter outline looks like this:

**`COVER_LETTER_OUTLINE.md`**

```markdown
Tempore et quis deleniti cumque, {}.

{} repudiandae fugit.

Et {} illo autem modi unde necessitatibus adipisci.
```

Notice how the example has 3 spots for company names in the outline.

Now, you need to go to [`apply.py`](./apply.py) and fill in the amount of times your `company_name` occurs in the outline.

> 💡 You can just search for "content = content.format" in `apply.py` to find it quicker

**`apply.py`**

```python
# Insert company name into template the number of times it occurs in the outline
content = content.format(company_name, company_name, company_name)
```

If we don't do this, the script will not compile, as we have a mismatch between the number of times the comapny name occurs in the outline and the number of times we insert it into the outline.

## Running the application ✅

This script uses [Weasyprint](https://weasyprint.org/) under the hood. Please ensure you have **[Pango](http://www.pango.org/)** installed. Pango helps with formatting HTML to PDF. If you have brew, use:

```sh
brew install pango
```

The script will not run otherwise.

After installing pango, please do the following:

```sh
# Navigate to the application directory
cd job-applier

# Create virtual environment
python3 -m venv venv

# Activate using Windows:
venv\Scripts\activate.bat

# OR

# Activate using Mac or Unix:
source venv/bin/activate

# Install requirements
python3 -m pip install -r requirements.txt
```

Now that everything is set up, you should be able to run the actual script to generate a PDF cover letter:

> ❗️ Note that you must use quotes around the company name

```sh
# Converts a .md file to PDF with the company name
python3 apply.py "company_name" cover_letter_outline

# Example
python3 apply.py "Google" COVER_LETTER_OUTLINE.md
```

## Adding styling to your cover letter 🎨

You can add your own `CSS` to the PDF result. I recommend starting with a blank `style.css`, and then building on the outcome from there.
