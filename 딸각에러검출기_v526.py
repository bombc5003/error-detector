import sys, os, subprocess, threading, winsound, time, re
import tkinter as tk
from tkinter import filedialog, scrolledtext

# 하이퍼 엔진 체크: 드롭 기능을 위한 라이브러리 자동 설치
def check_engine():
    try:
        import tkinterdnd2
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinterdnd2"])

check_engine()
from tkinterdnd2 import DND_FILES, TkinterDnD

class SentinelHyperAnalyzerV526:
    def __init__(self, root):
        self.root = root
        self.root.title("v526.3-H ANALYZER")
        self.root.geometry("390x330")
        self._last_target = None  # 마지막 실행 파일 경로 보존
        self.root.configure(bg="#000")
        self.root.attributes("-topmost", True)

        # 드롭 타겟 등록: 파일 던지기 활성화
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.handle_drop)

        # 헤더
        self.header = tk.Label(root, text="[ K-SENTINEL v526.3-H - HYPER ANALYZER ]", fg="#ffffff", bg="#b100e8", 
                               font=("Consolas", 8, "bold"), pady=5)
        self.header.pack(fill=tk.X)

        self.ctrl = tk.Frame(root, bg="#000")
        self.ctrl.pack(pady=5, fill=tk.X)
        
        btn_s = {"font": ("맑은 고딕", 7, "bold"), "height": 1}
        
        self.btn_pin = tk.Button(self.ctrl, text="📌", command=self.toggle_pin, **btn_s, width=2, bg="#222", fg="#0f0")
        self.btn_pin.pack(side=tk.LEFT, padx=1)
        self.btn_select = tk.Button(self.ctrl, text="📁파일", command=self.start_monitoring, **btn_s, width=6, bg="#004b96", fg="white")
        self.btn_select.pack(side=tk.LEFT, padx=1)
        self.btn_report = tk.Button(self.ctrl, text="🔍분석", command=self.run_real_analysis, **btn_s, width=6, bg="#d90429", fg="white")
        self.btn_report.pack(side=tk.LEFT, padx=1)
        self.btn_help = tk.Button(self.ctrl, text="🆘도움", command=self.get_real_help, **btn_s, width=6, bg="#ff0000", fg="white")
        self.btn_help.pack(side=tk.LEFT, padx=1)

        self.error_board = scrolledtext.ScrolledText(root, bg="#050505", fg="#00ff00", font=("Consolas", 8), borderwidth=0)
        self.error_board.pack(pady=5, padx=5, expand=True, fill=tk.BOTH)
        
        self.error_board.tag_config("err", foreground="#ff3333", font=("Consolas", 8, "bold"))
        self.last_error_log = ""
        self.log_to_board("v526.2-H READY. DROP PY FILE.")

    def log_to_board(self, content, tag=None):
        self.error_board.config(state=tk.NORMAL)
        self.error_board.insert(tk.END, f"> {content}\n", tag)
        self.error_board.see(tk.END)
        self.error_board.config(state=tk.DISABLED)

    def handle_drop(self, event):
        """ 드래그 앤 드롭 시 즉시 분석 실행 """
        files = self.root.tk.splitlist(event.data)
        if files:
            target = files[0]
            if target.lower().endswith('.py'):
                self.log_to_board(f"DROP DETECTED: {os.path.basename(target)}")
                winsound.Beep(800, 100)
                self.launch_target(target)
            else:
                self.log_to_board("ONLY .PY FILES SUPPORTED.", "err")

    def run_real_analysis(self):
        if not self.last_error_log:
            self.log_to_board("NO ERROR DETECTED YET.")
            return

        lines  = re.findall(r"line (\d+)", self.last_error_log)
        errors = re.findall(r"(\w+Error[^\s:]*|SyntaxError|IndentationError|ModuleNotFoundError): (.*)", self.last_error_log)
        missing = re.findall(r"No module named '([^']+)'", self.last_error_log)
        syntax_hint = re.findall(r"\^\s*\n\s*(\w+Error)", self.last_error_log)

        self.log_to_board("\n" + "━"*20)
        self.log_to_board("[ 정밀 분석 데이터 사출 ]", "err")
        if lines:   self.log_to_board(f"● 타격지점: {lines[-1]}번 라인")
        if errors:  self.log_to_board(f"● 원인코드: {errors[-1][0]}  →  {errors[-1][1][:80]}")
        if missing: self.log_to_board(f"● 미설치 모듈: {', '.join(missing)}")
        if syntax_hint: self.log_to_board(f"● 문법 오류 위치 감지: {syntax_hint[-1]}")

        # 오류 코드 클립보드 자동 복사
        try:
            clip_text = self.last_error_log[-500:]
            self.root.clipboard_clear()
            self.root.clipboard_append(clip_text)
            self.log_to_board("● 오류 로그 500자 클립보드 복사 완료")
        except Exception:
            pass

        self.log_to_board("━"*20)
        self.log_to_board(" [ 1인 개발자 — 개발비 후원 요망 ]")
        self.log_to_board(" 박병진: bc5103@naver.com")
        self.log_to_board(" 카카오페이·토스: 010-2272-7030")
        self.log_to_board(" ")
        self.log_to_board(" [ 포트폴리오 ]")
        self.log_to_board("  · 문서합체기 v1.0   PDF·이미지 병합")
        self.log_to_board("  · 딸깍 법무킷 v670  병합+찾기+증거목록+판례수집")
        self.log_to_board("  · 딸깍포렌식         크롬 확장 증거 보전 도구")
        self.log_to_board("  · ARGOS AI통합       다중 AI 통합 GUI")
        self.log_to_board("  · 딸각에러검출기      본 도구")
        self.log_to_board(" ")
        self.log_to_board(" 맞춤 프로그램 제작 문의 환영.")
        self.log_to_board("━"*20 + "\n")
        winsound.Beep(1200, 300)

    def launch_target(self, target):
        self.error_board.config(state=tk.NORMAL)
        self.error_board.delete(1.0, tk.END)
        self.error_board.config(state=tk.DISABLED)
        self.last_error_log = ""
        threading.Thread(target=self.execute_target, args=(target,), daemon=True).start()

    def execute_target(self, target_path):
        self._last_target = target_path  # 재실행용 경로 보존
        for enc in ('cp949', 'utf-8', 'utf-8-sig'):
            try:
                process = subprocess.Popen(
                    [sys.executable, "-u", target_path],
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    text=True, encoding=enc, errors='replace', bufsize=1)
                while True:
                    line = process.stdout.readline()
                    if not line and process.poll() is not None: break
                    if line:
                        is_err = "Error" in line or "Traceback" in line
                        if is_err: self.last_error_log += line
                        self.log_to_board(line.strip(), "err" if is_err else None)

                rc = process.returncode
                if rc != 0:
                    if not self.last_error_log:
                        # 에러 출력 없이 비정상 종료 — SILENT CRASH 탐지
                        silent_msg = f"SILENT CRASH  |  종료코드: {rc}"
                        self.last_error_log = silent_msg
                        self.log_to_board("━"*20)
                        self.log_to_board(f"SILENT CRASH  |  종료코드: {rc}", "err")
                        self.log_to_board("에러 출력 없이 비정상 종료 확인.", "err")
                        self.log_to_board("원인 후보:", "err")
                        self.log_to_board(f"  1. sys.exit({rc}) 직접 호출", "err")
                        self.log_to_board(f"  2. os._exit() 강제 종료", "err")
                        self.log_to_board(f"  3. 시그널(SIGKILL 등) 외부 강제 종료", "err")
                        self.log_to_board(f"  4. GUI 창 강제 닫기 (WM_DELETE_WINDOW 미처리)", "err")
                        self.log_to_board(f"  5. 스레드 내부 예외 (daemon thread 미포착)", "err")
                        self.log_to_board("━"*20)
                        winsound.Beep(600, 500)
                    else:
                        self.log_to_board(f"ABNORMAL EXIT  |  종료코드: {rc}", "err")
                else:
                    self.log_to_board(f"PROCESS EXIT NORMAL  |  종료코드: {rc}")
                return
            except UnicodeDecodeError:
                continue
            except Exception as e:
                self.log_to_board(f"EXEC ERR: {e}")
                return

    def self_patch(self):
        try:
            new_code = self.root.clipboard_get()
            if "import" not in new_code:
                self.log_to_board("PATCH ABORT: 클립보드에 유효한 코드 없음.")
                return
            from tkinter import messagebox
            if not messagebox.askyesno("패치 확인", "클립보드 코드로 현재 파일을 덮어씁니다.\n계속하시겠습니까?"):
                self.log_to_board("PATCH CANCELLED.")
                return
            path = os.path.abspath(sys.argv[0])
            with open(path, "w", encoding="utf-8") as f: f.write(new_code)
            self.log_to_board("PATCH SUCCESS. REBOOTING...")
            time.sleep(0.5); os.execl(sys.executable, sys.executable, path, *sys.argv[1:])
        except Exception as e:
            self.log_to_board(f"PATCH ERR: {e}")

    def rerun_last(self):
        if self._last_target and os.path.exists(self._last_target):
            self.log_to_board(N: {os.path.basename(self._last_target)}")
            self.launch_target(self._last_target)
        else:
            self.log_to_board("RERUN: 마지막 실행 파일 없음.")

    def start_monitoring(self):
        target = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if target: self.launch_target(target)

    def get_real_help(self):
        self.log_to_board("━"*20)
        self.log_to_board(" [ 1인 개발자 — 연구개발비 후원 요망 ]")
        self.log_to_board(" 혼자서 여러 프로그램을 만들고 있습니다.")
        self.log_to_board(" 후원해주시면 다음 개발에 큰 힘이 됩니다.")
        self.log_to_board(" ")
        self.log_to_board("  bc5103@naver.com")
        self.log_to_board("  카카오페이·토스: 010-2272-7030")
        self.log_to_board(" ")
        self.log_to_board(" [ 포트폴리오 ]")
        self.log_to_board("  · 문서합체기 v1.0    PDF·이미지 병합 (무료)")
        self.log_to_board("  · 딸깍 법무킷 v670   병합+찾기+증거목록+판례수집")
        self.log_to_board("  · 딸깍포렌식          크롬 확장 증거 보전 도구")
        self.log_to_board("  · ARGOS AI통합        다중 AI 통합 GUI")
        self.log_to_board("  · 딸각에러검출기       본 도구 (무료)")
        self.log_to_board(" ")
        self.log_to_board("莥度를 tlqkdrdg 이･ 스카웃 문의 환영.")
        self.log_to_board("━"*20)

    def toggle_pin(self):
        state = not self.root.attributes("-topmost")
        self.root.attributes("-topmost", state)
        self.btn_pin.config(fg="#0f0" if state else "#f00")

if __name__ == "__main__":
    root = TkinterDnD.Tk() # 마지막 실행 파일 경로 위한 TkinterDnD 사용
    app = SentinelHyperAnalyzerV526(root)
    root.mainloop()