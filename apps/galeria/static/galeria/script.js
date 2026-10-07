document.addEventListener("DOMContentLoaded", function () {
  const dropzone = document.getElementById("dropzone");
  const fileInput = document.getElementById("fileInput");
  const selectBtn = document.getElementById("selectBtn");
  const form = document.getElementById("upload-form");

  selectBtn.addEventListener("click", () => fileInput.click());

  dropzone.addEventListener("click", (e) => {
    if (e.target === selectBtn) return;
    fileInput.click();
  });

  // Assim que o usuário escolhe os arquivos, o form é enviado pro Django.
  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      form.submit();
    }
  });

  ["dragenter", "dragover"].forEach((evento) =>
    dropzone.addEventListener(evento, (e) => {
      e.preventDefault();
      dropzone.classList.add("drag-over");
    })
  );

  ["dragleave", "drop"].forEach((evento) =>
    dropzone.addEventListener(evento, (e) => {
      e.preventDefault();
      dropzone.classList.remove("drag-over");
    })
  );

  dropzone.addEventListener("drop", (e) => {
    const arquivos = e.dataTransfer.files;
    if (arquivos.length > 0) {
      fileInput.files = arquivos;
      form.submit();
    }
  });
});