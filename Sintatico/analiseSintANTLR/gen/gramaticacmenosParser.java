// Generated from /home/heuller/Documents/2019-1/Compiladores/analiseSintANTLR/src/gramaticacmenos.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class gramaticacmenosParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, T__55=56, T__56=57, T__57=58, T__58=59, 
		T__59=60, T__60=61, T__61=62, T__62=63, T__63=64, T__64=65, WS=66;
	public static final int
		RULE_programa = 0, RULE_declaracao_lista = 1, RULE_declaracao = 2, RULE_var_declaracao = 3, 
		RULE_tipo_especificador = 4, RULE_atributos_declaracao = 5, RULE_fun_declaracao = 6, 
		RULE_params = 7, RULE_param_lista = 8, RULE_param = 9, RULE_composto_decl = 10, 
		RULE_local_declaracoes = 11, RULE_comando_lista = 12, RULE_comando = 13, 
		RULE_expressao_decl = 14, RULE_selecao_decl = 15, RULE_iteracao_decl = 16, 
		RULE_retorno_decl = 17, RULE_expressao = 18, RULE_var = 19, RULE_expressao_simples = 20, 
		RULE_relacional = 21, RULE_expressao_soma = 22, RULE_soma = 23, RULE_termo = 24, 
		RULE_mult = 25, RULE_fator = 26, RULE_ativacao = 27, RULE_args = 28, RULE_arg_lista = 29, 
		RULE_num = 30, RULE_num_int = 31, RULE_digito = 32, RULE_ident = 33, RULE_letra = 34, 
		RULE_abre_chave = 35, RULE_fecha_chave = 36, RULE_abre_colchete = 37, 
		RULE_fecha_colchete = 38;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "declaracao_lista", "declaracao", "var_declaracao", "tipo_especificador", 
			"atributos_declaracao", "fun_declaracao", "params", "param_lista", "param", 
			"composto_decl", "local_declaracoes", "comando_lista", "comando", "expressao_decl", 
			"selecao_decl", "iteracao_decl", "retorno_decl", "expressao", "var", 
			"expressao_simples", "relacional", "expressao_soma", "soma", "termo", 
			"mult", "fator", "ativacao", "args", "arg_lista", "num", "num_int", "digito", 
			"ident", "letra", "abre_chave", "fecha_chave", "abre_colchete", "fecha_colchete"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'int'", "'float'", "'char'", "'void'", "'struct'", "'('", 
			"')'", "','", "'if'", "'else'", "'while'", "'return'", "'='", "'<='", 
			"'<'", "'>'", "'>='", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", "'.'", 
			"'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", 
			"'a'", "'b'", "'c'", "'d'", "'e'", "'f'", "'g'", "'h'", "'i'", "'j'", 
			"'k'", "'l'", "'m'", "'n'", "'o'", "'p'", "'q'", "'r'", "'s'", "'t'", 
			"'u'", "'v'", "'w'", "'x'", "'y'", "'z'", "'{'", "'}'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramaticacmenos.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticacmenosParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramaContext extends ParserRuleContext {
		public Declaracao_listaContext declaracao_lista() {
			return getRuleContext(Declaracao_listaContext.class,0);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitPrograma(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitPrograma(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			declaracao_lista();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Declaracao_listaContext extends ParserRuleContext {
		public List<DeclaracaoContext> declaracao() {
			return getRuleContexts(DeclaracaoContext.class);
		}
		public DeclaracaoContext declaracao(int i) {
			return getRuleContext(DeclaracaoContext.class,i);
		}
		public Declaracao_listaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao_lista; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterDeclaracao_lista(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitDeclaracao_lista(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitDeclaracao_lista(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Declaracao_listaContext declaracao_lista() throws RecognitionException {
		Declaracao_listaContext _localctx = new Declaracao_listaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaracao_lista);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(80);
				declaracao();
				}
				}
				setState(83); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclaracaoContext extends ParserRuleContext {
		public Var_declaracaoContext var_declaracao() {
			return getRuleContext(Var_declaracaoContext.class,0);
		}
		public Fun_declaracaoContext fun_declaracao() {
			return getRuleContext(Fun_declaracaoContext.class,0);
		}
		public DeclaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterDeclaracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitDeclaracao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitDeclaracao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DeclaracaoContext declaracao() throws RecognitionException {
		DeclaracaoContext _localctx = new DeclaracaoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaracao);
		try {
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(85);
				var_declaracao();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				fun_declaracao();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declaracaoContext extends ParserRuleContext {
		public Tipo_especificadorContext tipo_especificador() {
			return getRuleContext(Tipo_especificadorContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public List<Abre_colcheteContext> abre_colchete() {
			return getRuleContexts(Abre_colcheteContext.class);
		}
		public Abre_colcheteContext abre_colchete(int i) {
			return getRuleContext(Abre_colcheteContext.class,i);
		}
		public List<Num_intContext> num_int() {
			return getRuleContexts(Num_intContext.class);
		}
		public Num_intContext num_int(int i) {
			return getRuleContext(Num_intContext.class,i);
		}
		public List<Fecha_colcheteContext> fecha_colchete() {
			return getRuleContexts(Fecha_colcheteContext.class);
		}
		public Fecha_colcheteContext fecha_colchete(int i) {
			return getRuleContext(Fecha_colcheteContext.class,i);
		}
		public Var_declaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declaracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterVar_declaracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitVar_declaracao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitVar_declaracao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Var_declaracaoContext var_declaracao() throws RecognitionException {
		Var_declaracaoContext _localctx = new Var_declaracaoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_var_declaracao);
		int _la;
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				tipo_especificador();
				setState(90);
				ident();
				setState(91);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(93);
				tipo_especificador();
				setState(94);
				ident();
				setState(95);
				abre_colchete();
				setState(96);
				num_int();
				setState(97);
				fecha_colchete();
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__63) {
					{
					{
					setState(98);
					abre_colchete();
					setState(99);
					num_int();
					setState(100);
					fecha_colchete();
					}
					}
					setState(106);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Tipo_especificadorContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Abre_chaveContext abre_chave() {
			return getRuleContext(Abre_chaveContext.class,0);
		}
		public Atributos_declaracaoContext atributos_declaracao() {
			return getRuleContext(Atributos_declaracaoContext.class,0);
		}
		public Fecha_chaveContext fecha_chave() {
			return getRuleContext(Fecha_chaveContext.class,0);
		}
		public Tipo_especificadorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo_especificador; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterTipo_especificador(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitTipo_especificador(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitTipo_especificador(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Tipo_especificadorContext tipo_especificador() throws RecognitionException {
		Tipo_especificadorContext _localctx = new Tipo_especificadorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_tipo_especificador);
		try {
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				match(T__1);
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				match(T__2);
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 3);
				{
				setState(111);
				match(T__3);
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 4);
				{
				setState(112);
				match(T__4);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 5);
				{
				setState(113);
				match(T__5);
				setState(114);
				ident();
				setState(115);
				abre_chave();
				setState(116);
				atributos_declaracao();
				setState(117);
				fecha_chave();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Atributos_declaracaoContext extends ParserRuleContext {
		public List<Var_declaracaoContext> var_declaracao() {
			return getRuleContexts(Var_declaracaoContext.class);
		}
		public Var_declaracaoContext var_declaracao(int i) {
			return getRuleContext(Var_declaracaoContext.class,i);
		}
		public Atributos_declaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atributos_declaracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterAtributos_declaracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitAtributos_declaracao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitAtributos_declaracao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Atributos_declaracaoContext atributos_declaracao() throws RecognitionException {
		Atributos_declaracaoContext _localctx = new Atributos_declaracaoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_atributos_declaracao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			var_declaracao();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5))) != 0)) {
				{
				{
				setState(122);
				var_declaracao();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Fun_declaracaoContext extends ParserRuleContext {
		public Tipo_especificadorContext tipo_especificador() {
			return getRuleContext(Tipo_especificadorContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public Composto_declContext composto_decl() {
			return getRuleContext(Composto_declContext.class,0);
		}
		public Fun_declaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fun_declaracao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterFun_declaracao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitFun_declaracao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitFun_declaracao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Fun_declaracaoContext fun_declaracao() throws RecognitionException {
		Fun_declaracaoContext _localctx = new Fun_declaracaoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_fun_declaracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			tipo_especificador();
			setState(129);
			ident();
			setState(130);
			match(T__6);
			setState(131);
			params();
			setState(132);
			match(T__7);
			setState(133);
			composto_decl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamsContext extends ParserRuleContext {
		public Param_listaContext param_lista() {
			return getRuleContext(Param_listaContext.class,0);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterParams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitParams(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitParams(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_params);
		try {
			setState(137);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(135);
				param_lista();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				match(T__4);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_listaContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public Param_listaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_lista; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterParam_lista(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitParam_lista(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitParam_lista(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Param_listaContext param_lista() throws RecognitionException {
		Param_listaContext _localctx = new Param_listaContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_param_lista);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			param();
			setState(144);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__8) {
				{
				{
				setState(140);
				match(T__8);
				setState(141);
				param();
				}
				}
				setState(146);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public Tipo_especificadorContext tipo_especificador() {
			return getRuleContext(Tipo_especificadorContext.class,0);
		}
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public Abre_colcheteContext abre_colchete() {
			return getRuleContext(Abre_colcheteContext.class,0);
		}
		public Fecha_colcheteContext fecha_colchete() {
			return getRuleContext(Fecha_colcheteContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitParam(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitParam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_param);
		try {
			setState(155);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				tipo_especificador();
				setState(148);
				ident();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(150);
				tipo_especificador();
				setState(151);
				ident();
				setState(152);
				abre_colchete();
				setState(153);
				fecha_colchete();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Composto_declContext extends ParserRuleContext {
		public Abre_chaveContext abre_chave() {
			return getRuleContext(Abre_chaveContext.class,0);
		}
		public Local_declaracoesContext local_declaracoes() {
			return getRuleContext(Local_declaracoesContext.class,0);
		}
		public Comando_listaContext comando_lista() {
			return getRuleContext(Comando_listaContext.class,0);
		}
		public Fecha_chaveContext fecha_chave() {
			return getRuleContext(Fecha_chaveContext.class,0);
		}
		public Composto_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composto_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterComposto_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitComposto_decl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitComposto_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Composto_declContext composto_decl() throws RecognitionException {
		Composto_declContext _localctx = new Composto_declContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_composto_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			abre_chave();
			setState(158);
			local_declaracoes();
			setState(159);
			comando_lista();
			setState(160);
			fecha_chave();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Local_declaracoesContext extends ParserRuleContext {
		public List<Var_declaracaoContext> var_declaracao() {
			return getRuleContexts(Var_declaracaoContext.class);
		}
		public Var_declaracaoContext var_declaracao(int i) {
			return getRuleContext(Var_declaracaoContext.class,i);
		}
		public Local_declaracoesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_local_declaracoes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterLocal_declaracoes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitLocal_declaracoes(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitLocal_declaracoes(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Local_declaracoesContext local_declaracoes() throws RecognitionException {
		Local_declaracoesContext _localctx = new Local_declaracoesContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_local_declaracoes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5))) != 0)) {
				{
				{
				setState(162);
				var_declaracao();
				}
				}
				setState(167);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comando_listaContext extends ParserRuleContext {
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public Comando_listaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_lista; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterComando_lista(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitComando_lista(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitComando_lista(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Comando_listaContext comando_lista() throws RecognitionException {
		Comando_listaContext _localctx = new Comando_listaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_comando_lista);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << T__6) | (1L << T__9) | (1L << T__11) | (1L << T__12) | (1L << T__20) | (1L << T__21) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << T__41) | (1L << T__42) | (1L << T__43) | (1L << T__44) | (1L << T__45) | (1L << T__46) | (1L << T__47) | (1L << T__48) | (1L << T__49) | (1L << T__50) | (1L << T__51) | (1L << T__52) | (1L << T__53) | (1L << T__54) | (1L << T__55) | (1L << T__56) | (1L << T__57) | (1L << T__58) | (1L << T__59) | (1L << T__60) | (1L << T__61))) != 0)) {
				{
				{
				setState(168);
				comando();
				}
				}
				setState(173);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComandoContext extends ParserRuleContext {
		public Expressao_declContext expressao_decl() {
			return getRuleContext(Expressao_declContext.class,0);
		}
		public Composto_declContext composto_decl() {
			return getRuleContext(Composto_declContext.class,0);
		}
		public Selecao_declContext selecao_decl() {
			return getRuleContext(Selecao_declContext.class,0);
		}
		public Iteracao_declContext iteracao_decl() {
			return getRuleContext(Iteracao_declContext.class,0);
		}
		public Retorno_declContext retorno_decl() {
			return getRuleContext(Retorno_declContext.class,0);
		}
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterComando(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitComando(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitComando(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_comando);
		try {
			setState(179);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__6:
			case T__20:
			case T__21:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case T__41:
			case T__42:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
			case T__47:
			case T__48:
			case T__49:
			case T__50:
			case T__51:
			case T__52:
			case T__53:
			case T__54:
			case T__55:
			case T__56:
			case T__57:
			case T__58:
			case T__59:
			case T__60:
				enterOuterAlt(_localctx, 1);
				{
				setState(174);
				expressao_decl();
				}
				break;
			case T__61:
				enterOuterAlt(_localctx, 2);
				{
				setState(175);
				composto_decl();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 3);
				{
				setState(176);
				selecao_decl();
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 4);
				{
				setState(177);
				iteracao_decl();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 5);
				{
				setState(178);
				retorno_decl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expressao_declContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public Expressao_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterExpressao_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitExpressao_decl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitExpressao_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expressao_declContext expressao_decl() throws RecognitionException {
		Expressao_declContext _localctx = new Expressao_declContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expressao_decl);
		try {
			setState(185);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
			case T__20:
			case T__21:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
			case T__35:
			case T__36:
			case T__37:
			case T__38:
			case T__39:
			case T__40:
			case T__41:
			case T__42:
			case T__43:
			case T__44:
			case T__45:
			case T__46:
			case T__47:
			case T__48:
			case T__49:
			case T__50:
			case T__51:
			case T__52:
			case T__53:
			case T__54:
			case T__55:
			case T__56:
			case T__57:
			case T__58:
			case T__59:
			case T__60:
				enterOuterAlt(_localctx, 1);
				{
				setState(181);
				expressao();
				setState(182);
				match(T__0);
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 2);
				{
				setState(184);
				match(T__0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selecao_declContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public Selecao_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selecao_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterSelecao_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitSelecao_decl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitSelecao_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Selecao_declContext selecao_decl() throws RecognitionException {
		Selecao_declContext _localctx = new Selecao_declContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_selecao_decl);
		try {
			setState(201);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				match(T__9);
				setState(188);
				match(T__6);
				setState(189);
				expressao();
				setState(190);
				match(T__7);
				setState(191);
				comando();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(193);
				match(T__9);
				setState(194);
				match(T__6);
				setState(195);
				expressao();
				setState(196);
				match(T__7);
				setState(197);
				comando();
				setState(198);
				match(T__10);
				setState(199);
				comando();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Iteracao_declContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public ComandoContext comando() {
			return getRuleContext(ComandoContext.class,0);
		}
		public Iteracao_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iteracao_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterIteracao_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitIteracao_decl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitIteracao_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Iteracao_declContext iteracao_decl() throws RecognitionException {
		Iteracao_declContext _localctx = new Iteracao_declContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_iteracao_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(203);
			match(T__11);
			setState(204);
			match(T__6);
			setState(205);
			expressao();
			setState(206);
			match(T__7);
			setState(207);
			comando();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Retorno_declContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public Retorno_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retorno_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterRetorno_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitRetorno_decl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitRetorno_decl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Retorno_declContext retorno_decl() throws RecognitionException {
		Retorno_declContext _localctx = new Retorno_declContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_retorno_decl);
		try {
			setState(213);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(209);
				match(T__12);
				setState(210);
				match(T__0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
				match(T__12);
				setState(212);
				expressao();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressaoContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public Expressao_simplesContext expressao_simples() {
			return getRuleContext(Expressao_simplesContext.class,0);
		}
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterExpressao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitExpressao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitExpressao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_expressao);
		try {
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				var();
				setState(216);
				match(T__13);
				setState(217);
				expressao();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(219);
				expressao_simples();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public List<Abre_colcheteContext> abre_colchete() {
			return getRuleContexts(Abre_colcheteContext.class);
		}
		public Abre_colcheteContext abre_colchete(int i) {
			return getRuleContext(Abre_colcheteContext.class,i);
		}
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public List<Fecha_colcheteContext> fecha_colchete() {
			return getRuleContexts(Fecha_colcheteContext.class);
		}
		public Fecha_colcheteContext fecha_colchete(int i) {
			return getRuleContext(Fecha_colcheteContext.class,i);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitVar(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitVar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_var);
		int _la;
		try {
			setState(236);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				ident();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(223);
				ident();
				setState(224);
				abre_colchete();
				setState(225);
				expressao();
				setState(226);
				fecha_colchete();
				setState(233);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__63) {
					{
					{
					setState(227);
					abre_colchete();
					setState(228);
					expressao();
					setState(229);
					fecha_colchete();
					}
					}
					setState(235);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expressao_simplesContext extends ParserRuleContext {
		public List<Expressao_somaContext> expressao_soma() {
			return getRuleContexts(Expressao_somaContext.class);
		}
		public Expressao_somaContext expressao_soma(int i) {
			return getRuleContext(Expressao_somaContext.class,i);
		}
		public RelacionalContext relacional() {
			return getRuleContext(RelacionalContext.class,0);
		}
		public Expressao_simplesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_simples; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterExpressao_simples(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitExpressao_simples(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitExpressao_simples(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expressao_simplesContext expressao_simples() throws RecognitionException {
		Expressao_simplesContext _localctx = new Expressao_simplesContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_expressao_simples);
		try {
			setState(243);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(238);
				expressao_soma();
				setState(239);
				relacional();
				setState(240);
				expressao_soma();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(242);
				expressao_soma();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RelacionalContext extends ParserRuleContext {
		public RelacionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relacional; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterRelacional(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitRelacional(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitRelacional(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RelacionalContext relacional() throws RecognitionException {
		RelacionalContext _localctx = new RelacionalContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_relacional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18) | (1L << T__19))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expressao_somaContext extends ParserRuleContext {
		public List<TermoContext> termo() {
			return getRuleContexts(TermoContext.class);
		}
		public TermoContext termo(int i) {
			return getRuleContext(TermoContext.class,i);
		}
		public List<SomaContext> soma() {
			return getRuleContexts(SomaContext.class);
		}
		public SomaContext soma(int i) {
			return getRuleContext(SomaContext.class,i);
		}
		public Expressao_somaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao_soma; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterExpressao_soma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitExpressao_soma(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitExpressao_soma(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Expressao_somaContext expressao_soma() throws RecognitionException {
		Expressao_somaContext _localctx = new Expressao_somaContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_expressao_soma);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			termo();
			setState(253);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(248);
					soma();
					setState(249);
					termo();
					}
					} 
				}
				setState(255);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SomaContext extends ParserRuleContext {
		public SomaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_soma; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterSoma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitSoma(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitSoma(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SomaContext soma() throws RecognitionException {
		SomaContext _localctx = new SomaContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_soma);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			_la = _input.LA(1);
			if ( !(_la==T__20 || _la==T__21) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermoContext extends ParserRuleContext {
		public List<FatorContext> fator() {
			return getRuleContexts(FatorContext.class);
		}
		public FatorContext fator(int i) {
			return getRuleContext(FatorContext.class,i);
		}
		public List<MultContext> mult() {
			return getRuleContexts(MultContext.class);
		}
		public MultContext mult(int i) {
			return getRuleContext(MultContext.class,i);
		}
		public TermoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterTermo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitTermo(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitTermo(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TermoContext termo() throws RecognitionException {
		TermoContext _localctx = new TermoContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_termo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			fator();
			setState(264);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__22 || _la==T__23) {
				{
				{
				setState(259);
				mult();
				setState(260);
				fator();
				}
				}
				setState(266);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultContext extends ParserRuleContext {
		public MultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mult; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterMult(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitMult(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitMult(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MultContext mult() throws RecognitionException {
		MultContext _localctx = new MultContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_mult);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			_la = _input.LA(1);
			if ( !(_la==T__22 || _la==T__23) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FatorContext extends ParserRuleContext {
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public AtivacaoContext ativacao() {
			return getRuleContext(AtivacaoContext.class,0);
		}
		public NumContext num() {
			return getRuleContext(NumContext.class,0);
		}
		public Num_intContext num_int() {
			return getRuleContext(Num_intContext.class,0);
		}
		public FatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterFator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitFator(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitFator(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FatorContext fator() throws RecognitionException {
		FatorContext _localctx = new FatorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_fator);
		try {
			setState(277);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				match(T__6);
				setState(270);
				expressao();
				setState(271);
				match(T__7);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(273);
				var();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(274);
				ativacao();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(275);
				num();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(276);
				num_int();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtivacaoContext extends ParserRuleContext {
		public IdentContext ident() {
			return getRuleContext(IdentContext.class,0);
		}
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public AtivacaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ativacao; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterAtivacao(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitAtivacao(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitAtivacao(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtivacaoContext ativacao() throws RecognitionException {
		AtivacaoContext _localctx = new AtivacaoContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_ativacao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			ident();
			setState(280);
			match(T__6);
			setState(281);
			args();
			setState(282);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgsContext extends ParserRuleContext {
		public Arg_listaContext arg_lista() {
			return getRuleContext(Arg_listaContext.class,0);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterArgs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitArgs(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitArgs(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_args);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			arg_lista();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arg_listaContext extends ParserRuleContext {
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public Arg_listaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_lista; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterArg_lista(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitArg_lista(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitArg_lista(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Arg_listaContext arg_lista() throws RecognitionException {
		Arg_listaContext _localctx = new Arg_listaContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_arg_lista);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			expressao();
			setState(291);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__8) {
				{
				{
				setState(287);
				match(T__8);
				setState(288);
				expressao();
				}
				}
				setState(293);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumContext extends ParserRuleContext {
		public SomaContext soma() {
			return getRuleContext(SomaContext.class,0);
		}
		public List<DigitoContext> digito() {
			return getRuleContexts(DigitoContext.class);
		}
		public DigitoContext digito(int i) {
			return getRuleContext(DigitoContext.class,i);
		}
		public NumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterNum(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitNum(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitNum(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NumContext num() throws RecognitionException {
		NumContext _localctx = new NumContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_num);
		try {
			int _alt;
			setState(325);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
			case T__21:
				enterOuterAlt(_localctx, 1);
				{
				setState(294);
				soma();
				setState(295);
				digito();
				setState(307);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(296);
						digito();
						setState(297);
						match(T__24);
						setState(298);
						digito();
						setState(302);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
						while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
							if ( _alt==1 ) {
								{
								{
								setState(299);
								digito();
								}
								} 
							}
							setState(304);
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
						}
						}
						} 
					}
					setState(309);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
				}
				}
				break;
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__32:
			case T__33:
			case T__34:
				enterOuterAlt(_localctx, 2);
				{
				setState(310);
				digito();
				setState(322);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(311);
						digito();
						setState(312);
						match(T__24);
						setState(313);
						digito();
						setState(317);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
						while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
							if ( _alt==1 ) {
								{
								{
								setState(314);
								digito();
								}
								} 
							}
							setState(319);
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
						}
						}
						} 
					}
					setState(324);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Num_intContext extends ParserRuleContext {
		public List<DigitoContext> digito() {
			return getRuleContexts(DigitoContext.class);
		}
		public DigitoContext digito(int i) {
			return getRuleContext(DigitoContext.class,i);
		}
		public Num_intContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num_int; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterNum_int(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitNum_int(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitNum_int(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Num_intContext num_int() throws RecognitionException {
		Num_intContext _localctx = new Num_intContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_num_int);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			digito();
			setState(331);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(328);
					digito();
					}
					} 
				}
				setState(333);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,28,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DigitoContext extends ParserRuleContext {
		public DigitoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_digito; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterDigito(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitDigito(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitDigito(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DigitoContext digito() throws RecognitionException {
		DigitoContext _localctx = new DigitoContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_digito);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentContext extends ParserRuleContext {
		public List<LetraContext> letra() {
			return getRuleContexts(LetraContext.class);
		}
		public LetraContext letra(int i) {
			return getRuleContext(LetraContext.class,i);
		}
		public List<DigitoContext> digito() {
			return getRuleContexts(DigitoContext.class);
		}
		public DigitoContext digito(int i) {
			return getRuleContext(DigitoContext.class,i);
		}
		public IdentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ident; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterIdent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitIdent(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitIdent(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentContext ident() throws RecognitionException {
		IdentContext _localctx = new IdentContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_ident);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			letra();
			setState(341);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					setState(339);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case T__35:
					case T__36:
					case T__37:
					case T__38:
					case T__39:
					case T__40:
					case T__41:
					case T__42:
					case T__43:
					case T__44:
					case T__45:
					case T__46:
					case T__47:
					case T__48:
					case T__49:
					case T__50:
					case T__51:
					case T__52:
					case T__53:
					case T__54:
					case T__55:
					case T__56:
					case T__57:
					case T__58:
					case T__59:
					case T__60:
						{
						setState(337);
						letra();
						}
						break;
					case T__25:
					case T__26:
					case T__27:
					case T__28:
					case T__29:
					case T__30:
					case T__31:
					case T__32:
					case T__33:
					case T__34:
						{
						setState(338);
						digito();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					} 
				}
				setState(343);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LetraContext extends ParserRuleContext {
		public LetraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letra; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterLetra(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitLetra(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitLetra(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LetraContext letra() throws RecognitionException {
		LetraContext _localctx = new LetraContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_letra);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(344);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << T__41) | (1L << T__42) | (1L << T__43) | (1L << T__44) | (1L << T__45) | (1L << T__46) | (1L << T__47) | (1L << T__48) | (1L << T__49) | (1L << T__50) | (1L << T__51) | (1L << T__52) | (1L << T__53) | (1L << T__54) | (1L << T__55) | (1L << T__56) | (1L << T__57) | (1L << T__58) | (1L << T__59) | (1L << T__60))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Abre_chaveContext extends ParserRuleContext {
		public Abre_chaveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_abre_chave; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterAbre_chave(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitAbre_chave(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitAbre_chave(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Abre_chaveContext abre_chave() throws RecognitionException {
		Abre_chaveContext _localctx = new Abre_chaveContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_abre_chave);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(346);
			match(T__61);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Fecha_chaveContext extends ParserRuleContext {
		public Fecha_chaveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fecha_chave; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterFecha_chave(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitFecha_chave(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitFecha_chave(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Fecha_chaveContext fecha_chave() throws RecognitionException {
		Fecha_chaveContext _localctx = new Fecha_chaveContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_fecha_chave);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(T__62);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Abre_colcheteContext extends ParserRuleContext {
		public Abre_colcheteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_abre_colchete; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterAbre_colchete(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitAbre_colchete(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitAbre_colchete(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Abre_colcheteContext abre_colchete() throws RecognitionException {
		Abre_colcheteContext _localctx = new Abre_colcheteContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_abre_colchete);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			match(T__63);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Fecha_colcheteContext extends ParserRuleContext {
		public Fecha_colcheteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fecha_colchete; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).enterFecha_colchete(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof gramaticacmenosListener ) ((gramaticacmenosListener)listener).exitFecha_colchete(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof gramaticacmenosVisitor ) return ((gramaticacmenosVisitor<? extends T>)visitor).visitFecha_colchete(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Fecha_colcheteContext fecha_colchete() throws RecognitionException {
		Fecha_colcheteContext _localctx = new Fecha_colcheteContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_fecha_colchete);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(352);
			match(T__64);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D\u0165\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\3\6\3T\n\3"+
		"\r\3\16\3U\3\4\3\4\5\4Z\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\7\5i\n\5\f\5\16\5l\13\5\5\5n\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\5\6z\n\6\3\7\3\7\7\7~\n\7\f\7\16\7\u0081\13\7\3\b\3\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u008c\n\t\3\n\3\n\3\n\7\n\u0091\n\n\f\n"+
		"\16\n\u0094\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009e\n"+
		"\13\3\f\3\f\3\f\3\f\3\f\3\r\7\r\u00a6\n\r\f\r\16\r\u00a9\13\r\3\16\7\16"+
		"\u00ac\n\16\f\16\16\16\u00af\13\16\3\17\3\17\3\17\3\17\3\17\5\17\u00b6"+
		"\n\17\3\20\3\20\3\20\3\20\5\20\u00bc\n\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00cc\n\21\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00d8\n\23\3\24\3\24\3\24\3\24"+
		"\3\24\5\24\u00df\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25"+
		"\u00ea\n\25\f\25\16\25\u00ed\13\25\5\25\u00ef\n\25\3\26\3\26\3\26\3\26"+
		"\3\26\5\26\u00f6\n\26\3\27\3\27\3\30\3\30\3\30\3\30\7\30\u00fe\n\30\f"+
		"\30\16\30\u0101\13\30\3\31\3\31\3\32\3\32\3\32\3\32\7\32\u0109\n\32\f"+
		"\32\16\32\u010c\13\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\5\34\u0118\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\7\37"+
		"\u0124\n\37\f\37\16\37\u0127\13\37\3 \3 \3 \3 \3 \3 \7 \u012f\n \f \16"+
		" \u0132\13 \7 \u0134\n \f \16 \u0137\13 \3 \3 \3 \3 \3 \7 \u013e\n \f"+
		" \16 \u0141\13 \7 \u0143\n \f \16 \u0146\13 \5 \u0148\n \3!\3!\7!\u014c"+
		"\n!\f!\16!\u014f\13!\3\"\3\"\3#\3#\3#\7#\u0156\n#\f#\16#\u0159\13#\3$"+
		"\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\2\2)\2\4\6\b\n\f\16\20\22\24\26\30\32"+
		"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLN\2\7\3\2\21\26\3\2\27\30\3\2\31"+
		"\32\3\2\34%\3\2&?\2\u0165\2P\3\2\2\2\4S\3\2\2\2\6Y\3\2\2\2\bm\3\2\2\2"+
		"\ny\3\2\2\2\f{\3\2\2\2\16\u0082\3\2\2\2\20\u008b\3\2\2\2\22\u008d\3\2"+
		"\2\2\24\u009d\3\2\2\2\26\u009f\3\2\2\2\30\u00a7\3\2\2\2\32\u00ad\3\2\2"+
		"\2\34\u00b5\3\2\2\2\36\u00bb\3\2\2\2 \u00cb\3\2\2\2\"\u00cd\3\2\2\2$\u00d7"+
		"\3\2\2\2&\u00de\3\2\2\2(\u00ee\3\2\2\2*\u00f5\3\2\2\2,\u00f7\3\2\2\2."+
		"\u00f9\3\2\2\2\60\u0102\3\2\2\2\62\u0104\3\2\2\2\64\u010d\3\2\2\2\66\u0117"+
		"\3\2\2\28\u0119\3\2\2\2:\u011e\3\2\2\2<\u0120\3\2\2\2>\u0147\3\2\2\2@"+
		"\u0149\3\2\2\2B\u0150\3\2\2\2D\u0152\3\2\2\2F\u015a\3\2\2\2H\u015c\3\2"+
		"\2\2J\u015e\3\2\2\2L\u0160\3\2\2\2N\u0162\3\2\2\2PQ\5\4\3\2Q\3\3\2\2\2"+
		"RT\5\6\4\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V\5\3\2\2\2WZ\5\b\5"+
		"\2XZ\5\16\b\2YW\3\2\2\2YX\3\2\2\2Z\7\3\2\2\2[\\\5\n\6\2\\]\5D#\2]^\7\3"+
		"\2\2^n\3\2\2\2_`\5\n\6\2`a\5D#\2ab\5L\'\2bc\5@!\2cj\5N(\2de\5L\'\2ef\5"+
		"@!\2fg\5N(\2gi\3\2\2\2hd\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2kn\3\2\2"+
		"\2lj\3\2\2\2m[\3\2\2\2m_\3\2\2\2n\t\3\2\2\2oz\7\4\2\2pz\7\5\2\2qz\7\6"+
		"\2\2rz\7\7\2\2st\7\b\2\2tu\5D#\2uv\5H%\2vw\5\f\7\2wx\5J&\2xz\3\2\2\2y"+
		"o\3\2\2\2yp\3\2\2\2yq\3\2\2\2yr\3\2\2\2ys\3\2\2\2z\13\3\2\2\2{\177\5\b"+
		"\5\2|~\5\b\5\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2"+
		"\u0080\r\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\5\n\6\2\u0083\u0084\5D"+
		"#\2\u0084\u0085\7\t\2\2\u0085\u0086\5\20\t\2\u0086\u0087\7\n\2\2\u0087"+
		"\u0088\5\26\f\2\u0088\17\3\2\2\2\u0089\u008c\5\22\n\2\u008a\u008c\7\7"+
		"\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\21\3\2\2\2\u008d\u0092"+
		"\5\24\13\2\u008e\u008f\7\13\2\2\u008f\u0091\5\24\13\2\u0090\u008e\3\2"+
		"\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093"+
		"\23\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\5\n\6\2\u0096\u0097\5D#\2"+
		"\u0097\u009e\3\2\2\2\u0098\u0099\5\n\6\2\u0099\u009a\5D#\2\u009a\u009b"+
		"\5L\'\2\u009b\u009c\5N(\2\u009c\u009e\3\2\2\2\u009d\u0095\3\2\2\2\u009d"+
		"\u0098\3\2\2\2\u009e\25\3\2\2\2\u009f\u00a0\5H%\2\u00a0\u00a1\5\30\r\2"+
		"\u00a1\u00a2\5\32\16\2\u00a2\u00a3\5J&\2\u00a3\27\3\2\2\2\u00a4\u00a6"+
		"\5\b\5\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7"+
		"\u00a8\3\2\2\2\u00a8\31\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ac\5\34\17"+
		"\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae"+
		"\3\2\2\2\u00ae\33\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b6\5\36\20\2\u00b1"+
		"\u00b6\5\26\f\2\u00b2\u00b6\5 \21\2\u00b3\u00b6\5\"\22\2\u00b4\u00b6\5"+
		"$\23\2\u00b5\u00b0\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b5"+
		"\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\35\3\2\2\2\u00b7\u00b8\5&\24"+
		"\2\u00b8\u00b9\7\3\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc\7\3\2\2\u00bb\u00b7"+
		"\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\37\3\2\2\2\u00bd\u00be\7\f\2\2\u00be"+
		"\u00bf\7\t\2\2\u00bf\u00c0\5&\24\2\u00c0\u00c1\7\n\2\2\u00c1\u00c2\5\34"+
		"\17\2\u00c2\u00cc\3\2\2\2\u00c3\u00c4\7\f\2\2\u00c4\u00c5\7\t\2\2\u00c5"+
		"\u00c6\5&\24\2\u00c6\u00c7\7\n\2\2\u00c7\u00c8\5\34\17\2\u00c8\u00c9\7"+
		"\r\2\2\u00c9\u00ca\5\34\17\2\u00ca\u00cc\3\2\2\2\u00cb\u00bd\3\2\2\2\u00cb"+
		"\u00c3\3\2\2\2\u00cc!\3\2\2\2\u00cd\u00ce\7\16\2\2\u00ce\u00cf\7\t\2\2"+
		"\u00cf\u00d0\5&\24\2\u00d0\u00d1\7\n\2\2\u00d1\u00d2\5\34\17\2\u00d2#"+
		"\3\2\2\2\u00d3\u00d4\7\17\2\2\u00d4\u00d8\7\3\2\2\u00d5\u00d6\7\17\2\2"+
		"\u00d6\u00d8\5&\24\2\u00d7\u00d3\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8%\3"+
		"\2\2\2\u00d9\u00da\5(\25\2\u00da\u00db\7\20\2\2\u00db\u00dc\5&\24\2\u00dc"+
		"\u00df\3\2\2\2\u00dd\u00df\5*\26\2\u00de\u00d9\3\2\2\2\u00de\u00dd\3\2"+
		"\2\2\u00df\'\3\2\2\2\u00e0\u00ef\5D#\2\u00e1\u00e2\5D#\2\u00e2\u00e3\5"+
		"L\'\2\u00e3\u00e4\5&\24\2\u00e4\u00eb\5N(\2\u00e5\u00e6\5L\'\2\u00e6\u00e7"+
		"\5&\24\2\u00e7\u00e8\5N(\2\u00e8\u00ea\3\2\2\2\u00e9\u00e5\3\2\2\2\u00ea"+
		"\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ef\3\2"+
		"\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00e0\3\2\2\2\u00ee\u00e1\3\2\2\2\u00ef"+
		")\3\2\2\2\u00f0\u00f1\5.\30\2\u00f1\u00f2\5,\27\2\u00f2\u00f3\5.\30\2"+
		"\u00f3\u00f6\3\2\2\2\u00f4\u00f6\5.\30\2\u00f5\u00f0\3\2\2\2\u00f5\u00f4"+
		"\3\2\2\2\u00f6+\3\2\2\2\u00f7\u00f8\t\2\2\2\u00f8-\3\2\2\2\u00f9\u00ff"+
		"\5\62\32\2\u00fa\u00fb\5\60\31\2\u00fb\u00fc\5\62\32\2\u00fc\u00fe\3\2"+
		"\2\2\u00fd\u00fa\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff"+
		"\u0100\3\2\2\2\u0100/\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\t\3\2\2"+
		"\u0103\61\3\2\2\2\u0104\u010a\5\66\34\2\u0105\u0106\5\64\33\2\u0106\u0107"+
		"\5\66\34\2\u0107\u0109\3\2\2\2\u0108\u0105\3\2\2\2\u0109\u010c\3\2\2\2"+
		"\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\63\3\2\2\2\u010c\u010a"+
		"\3\2\2\2\u010d\u010e\t\4\2\2\u010e\65\3\2\2\2\u010f\u0110\7\t\2\2\u0110"+
		"\u0111\5&\24\2\u0111\u0112\7\n\2\2\u0112\u0118\3\2\2\2\u0113\u0118\5("+
		"\25\2\u0114\u0118\58\35\2\u0115\u0118\5> \2\u0116\u0118\5@!\2\u0117\u010f"+
		"\3\2\2\2\u0117\u0113\3\2\2\2\u0117\u0114\3\2\2\2\u0117\u0115\3\2\2\2\u0117"+
		"\u0116\3\2\2\2\u0118\67\3\2\2\2\u0119\u011a\5D#\2\u011a\u011b\7\t\2\2"+
		"\u011b\u011c\5:\36\2\u011c\u011d\7\n\2\2\u011d9\3\2\2\2\u011e\u011f\5"+
		"<\37\2\u011f;\3\2\2\2\u0120\u0125\5&\24\2\u0121\u0122\7\13\2\2\u0122\u0124"+
		"\5&\24\2\u0123\u0121\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125"+
		"\u0126\3\2\2\2\u0126=\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\5\60\31"+
		"\2\u0129\u0135\5B\"\2\u012a\u012b\5B\"\2\u012b\u012c\7\33\2\2\u012c\u0130"+
		"\5B\"\2\u012d\u012f\5B\"\2\u012e\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130"+
		"\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2"+
		"\2\2\u0133\u012a\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135"+
		"\u0136\3\2\2\2\u0136\u0148\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0144\5B"+
		"\"\2\u0139\u013a\5B\"\2\u013a\u013b\7\33\2\2\u013b\u013f\5B\"\2\u013c"+
		"\u013e\5B\"\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2"+
		"\2\2\u013f\u0140\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0142"+
		"\u0139\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2"+
		"\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0128\3\2\2\2\u0147"+
		"\u0138\3\2\2\2\u0148?\3\2\2\2\u0149\u014d\5B\"\2\u014a\u014c\5B\"\2\u014b"+
		"\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2"+
		"\2\2\u014eA\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\t\5\2\2\u0151C\3\2"+
		"\2\2\u0152\u0157\5F$\2\u0153\u0156\5F$\2\u0154\u0156\5B\"\2\u0155\u0153"+
		"\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157"+
		"\u0158\3\2\2\2\u0158E\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\t\6\2\2"+
		"\u015bG\3\2\2\2\u015c\u015d\7@\2\2\u015dI\3\2\2\2\u015e\u015f\7A\2\2\u015f"+
		"K\3\2\2\2\u0160\u0161\7B\2\2\u0161M\3\2\2\2\u0162\u0163\7C\2\2\u0163O"+
		"\3\2\2\2!UYjmy\177\u008b\u0092\u009d\u00a7\u00ad\u00b5\u00bb\u00cb\u00d7"+
		"\u00de\u00eb\u00ee\u00f5\u00ff\u010a\u0117\u0125\u0130\u0135\u013f\u0144"+
		"\u0147\u014d\u0155\u0157";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}