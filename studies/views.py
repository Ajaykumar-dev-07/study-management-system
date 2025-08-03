#views.py

import logging  # Make sure this line is at the top
from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm
from django.http import Http404

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class StudyManager:
    def add_study(self, study_name, description, phase, sponsor):
        try:
            study = Study(study_name=study_name, study_description=description, study_phase=phase, sponsor_name=sponsor)
            study.save()
            logging.info(f"Study '{study_name}' has been added successfully.")
            return study
        except Exception as e:
            logging.error(f"Error adding study '{study_name}': {e}")
            raise

    def edit_study(self, study_id, study_name, description, phase, sponsor):
        try:
            study = get_object_or_404(Study, id=study_id)
            study.study_name = study_name
            study.study_description = description
            study.study_phase = phase
            study.sponsor_name = sponsor
            study.save()
            logging.info(f"Study '{study_name}' (ID: {study_id}) has been edited successfully.")
            return study
        except Study.DoesNotExist:
            logging.error(f"Study with ID {study_id} does not exist.")
            raise Http404("Study not found.")
        except Exception as e:
            logging.error(f"Error editing study '{study_name}': {e}")
            raise

    def delete_study(self, study_id):
        try:
            study = get_object_or_404(Study, id=study_id)
            study_name = study.study_name
            study.delete()
            logging.info(f"Study '{study_name}' (ID: {study_id}) has been deleted.")
        except Study.DoesNotExist:
            logging.error(f"Study with ID {study_id} does not exist.")
            raise Http404("Study not found.")
        except Exception as e:
            logging.error(f"Error deleting study with ID {study_id}: {e}")
            raise

    def view_all_studies(self):
        try:
            studies = Study.objects.all()
            logging.info(f"Fetched all studies.")
            return studies
        except Exception as e:
            logging.error(f"Error fetching studies: {e}")
            raise

    def selected_view(self, study_id):
        try:
            study = get_object_or_404(Study, id=study_id)
            logging.info(f"Viewing details for Study ID {study_id}.")
            return study
        except Study.DoesNotExist:
            logging.error(f"Study with ID {study_id} does not exist.")
            raise Http404("Study not found.")
        except Exception as e:
            logging.error(f"Error fetching study with ID {study_id}: {e}")
            raise


# Views using StudyManager class
def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                logging.info("New study added successfully.")
                return redirect('view_all_studies')
            except Exception as e:
                logging.error(f"Error saving new study: {e}")
    else:
        form = StudyForm()
    return render(request, 'add.html', {'form': form})


def edit_study(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        if request.method == 'POST':
            form = StudyForm(request.POST, instance=study)
            if form.is_valid():
                form.save()
                logging.info(f"Study ID {study_id} updated successfully.")
                return redirect('view_all_studies')
        else:
            form = StudyForm(instance=study)
        return render(request, 'edit.html', {'form': form})
    except Http404 as e:
        logging.error(f"Study with ID {study_id} not found: {e}")
        raise
    except Exception as e:
        logging.error(f"Error updating study with ID {study_id}: {e}")
        raise


def delete_study(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        if request.method == 'POST':
            study.delete()
            logging.info(f"Study ID {study_id} deleted successfully.")
            return redirect('view_all_studies')
        return render(request, 'delete.html', {'study': study})
    except Http404 as e:
        logging.error(f"Study with ID {study_id} not found: {e}")
        raise
    except Exception as e:
        logging.error(f"Error deleting study with ID {study_id}: {e}")
        raise


def view_all_studies(request):
    try:
        studies = Study.objects.all()
        logging.info("All studies viewed.")
        return render(request, 'view.html', {'studies': studies})
    except Exception as e:
        logging.error(f"Error viewing all studies: {e}")
        raise


def selected_view(request, study_id):
    try:
        study = get_object_or_404(Study, id=study_id)
        logging.info(f"Viewing Study ID {study_id}.")
        return render(request, 'selected_view.html', {'study': study})
    except Http404 as e:
        logging.error(f"Study with ID {study_id} not found: {e}")
        raise
    except Exception as e:
        logging.error(f"Error fetching details for Study ID {study_id}: {e}")
        raise
