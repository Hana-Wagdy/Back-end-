document.getElementById('addBookForm')?.addEventListener('submit', function(e) {
  e.preventDefault();

  // Helper functions (keep these as they are)
  const getValue = (id, defaultValue = 'N/A') => {
    const element = document.getElementById(id);
    return element ? (element.value.trim() || defaultValue) : defaultValue;
  };

  const getFileName = (id) => {
    const element = document.getElementById(id);
    return (element && element.files.length > 0) ? element.files[0].name : null;
  };

  const books = JSON.parse(localStorage.getItem('books')) || [];
  
  const newId = books.length > 0 ? Math.max(...books.map(book => parseInt(book.id))) + 1 : 1;

  const coverFileName = getFileName('coverImage');
  const coverPath = coverFileName ? 'photos/' + coverFileName : 'photos/default-cover.jpg';

  const newBook = {
    id: newId.toString(),
    title: getValue('bookName', 'Untitled'),
    author: getValue('author'),
    isbn: getValue('isbn'),
    year: getValue('year'),
    publisher: getValue('publisher'),
    language: getValue('language', 'English'),
    category: getValue('category', 'Uncategorized'),
    description: getValue('description', 'No description provided'),
    cover: coverPath, 
    pdf: getFileName('pdfFile'),
    available: true,
    edition: {
      originalPublisher: getValue('originallyPublished'),
      publishedIn: getValue('publishedIn'),
      series: getValue('series'),
      deweyDecimal: getValue('deweyDecimal'),
      pages: getValue('pages')
    },
    identifiers: {
      openLibrary: getValue('openLibraryId'),
      internetArchive: getValue('internetArchive'),
      isbn10: getValue('isbn10'),
      libraryThing: getValue('libraryThing'),
      goodreads: getValue('goodreadsId'),
      workId: getValue('workId')
    }
  };

  // Save to localStorage
  books.push(newBook);
  localStorage.setItem('books', JSON.stringify(books));

  // Show success message and redirect
  alert('✅ Book added successfully!');
  window.location.href = "ManageBooks.html";
});